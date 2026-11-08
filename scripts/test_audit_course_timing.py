"""Regression checks for Reveal.js timing classification and exclusions."""

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "course_timing", Path(__file__).with_name("audit-course-timing.py")
)
TIMING = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TIMING)


class TimingTests(unittest.TestCase):
    def test_explicit_activity_allocation_overrides_diagram(self):
        slide = '<section data-duration-minutes="2"><h2>Case</h2><svg></svg></section>'
        self.assertEqual(TIMING.classify(slide)[2:], (2, 2, 2))

    def test_zero_contact_allocation_is_preserved(self):
        slide = '<section data-duration-minutes="0"><h2>Connect</h2></section>'
        self.assertEqual(TIMING.classify(slide)[1:], ("Contact", 0, 0, 0))

    def test_divider_slide_has_zero_timing(self):
        slide = '<section class="divider" data-duration-minutes="0"><h1>Topic</h1><h2>Subtitle</h2></section>'
        self.assertEqual(TIMING.classify(slide), ("Topic", "Divider", 0, 0, 0))

    def test_mapping_table_is_not_a_lab_launch(self):
        slide = "<section><h2>Lab 09 steps and the Harness platform</h2><table></table></section>"
        self.assertEqual(TIMING.classify(slide)[1], "Dense content")
        launch = "<section><h2>Lab 09: Delivery</h2></section>"
        self.assertEqual(TIMING.classify(launch)[1], "Lab launch")

    def test_speaker_notes_do_not_make_a_content_slide_dense(self):
        slide = "<section><h2>Rule</h2><p>One rule.</p><aside>" + "word " * 100 + "</aside></section>"
        self.assertEqual(TIMING.classify(slide)[1], "Content")

    def test_skip_and_reference_preserve_gross_time(self):
        html = (
            '<section data-duration-minutes="2"><h2>Retail</h2>'
            '<div class="skip-badge">SKIP</div></section>'
            '<section><h2>Extra detail</h2>'
            '<div class="reference-badge">REFERENCE ONLY</div></section>'
            '<section data-duration-minutes="5"><h2>Quiz</h2></section>'
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            slides = root / "slides"
            slides.mkdir(parents=True)
            for day in range(1, 4):
                (slides / f"day{day}.html").write_text(html)
            with patch.object(TIMING, "ROOT", root):
                results = TIMING.audit()
        self.assertEqual(len(results), 3)
        for _, _, rows in results:
            self.assertEqual(sum(row[3] for row in rows), 8.25)
            self.assertEqual(sum(row[4] for row in rows), 3.25)
            self.assertEqual(sum(row[5] for row in rows), 5)
            for row in rows:
                self.assertEqual(row[3], row[4] + row[5])
            self.assertEqual(rows[0][6:], (0, 0))
            self.assertEqual(rows[1][6:], (0, 0))


if __name__ == "__main__":
    unittest.main()
