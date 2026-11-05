# Viewing speaker notes during a lecture

This instructor-only guide covers the Day 1 HTML deck at [`devops-demos/slides/day1.html`](../devops-demos/slides/day1.html). Use the HTML presentation rather than an exported PDF or PowerPoint file.

The deck already uses Reveal.js 5.2.1, includes notes in `<aside class="notes">` elements, and enables the `RevealNotes` plugin. No changes to the deck are required. Speaker view opens in a separate window with the current slide, an upcoming-slide preview, notes, a clock, and a presentation timer.

## Quick start

1. Open Terminal and run the following command. Python 3 must be installed.

   ```bash
   python3 -m http.server 8000 --bind 127.0.0.1 --directory "/Users/kangs/code/github/intermediate-devops/devops-demos/slides"
   ```

2. Leave that Terminal window running. Open this address in Chrome, Edge, or Firefox:

   ```text
   http://127.0.0.1:8000/day1.html
   ```

3. Click the slide area so the presentation has keyboard focus, then press `S` without Command or Control.
4. Allow pop-ups for `http://127.0.0.1:8000` if the browser blocks the new window. Return to the slide window and press `S` again.
5. In the new speaker-view window, check that the first slide's notes begin with "Welcome everyone." Advance one slide in the main presentation window and confirm that the notes update.

Use the HTTP address above rather than double-clicking `day1.html`. Opening the deck as a `file://` URL can prevent speaker view from working because of browser security restrictions.

The server is bound to your computer's loopback address, so participants cannot access it over the classroom network. It serves only the slides directory. The deck loads Reveal.js from `cdn.jsdelivr.net`, so it still needs internet access; the local server does not make it fully offline.

## Choose what the audience sees

There are two separate windows:

| Window | Contents | Who should see it |
| --- | --- | --- |
| Main presentation | Slides without speaker notes | Audience |
| Speaker view | Slide previews, notes, clock, and timer | Instructor only |

Do not share or project speaker view. Keep it open on your private display.

### Classroom with a projector or second monitor

1. Connect the external display.
2. On macOS, open System Settings > Displays and configure the external screen as an extended display rather than a mirror. On Windows, press `Windows+P` and choose Extend.
3. Move the main presentation window to the projector or audience display.
4. Keep speaker view on your laptop display.
5. Click the main presentation and press `F` to request full-screen mode, if desired. Allow it if the browser asks.
6. Check the projected image before starting: only the slide should be visible, with no notes or speaker-view controls.

Mirroring shows the same desktop on both screens and can expose your notes. Use an extended desktop when you need a private presenter display.

### Online lecture using Zoom, Teams, or similar software

1. Open the slides and speaker view before starting screen sharing.
2. Share only the main presentation window, not your entire desktop and not the speaker-view window.
3. Keep speaker view visible on your own screen. With one monitor, arrange the two windows side by side; with two monitors, keep speaker view on the unshared display.
4. Check the meeting application's sharing preview or ask a co-host to confirm that the audience sees only slides.
5. Before switching to a terminal, lab, or other demo, pause or stop sharing, choose the intended demo window, and check the preview again.

If the meeting application only supports sharing an entire screen, dedicate that screen to audience content and keep notes on a different, unshared display. Do not put private notes on a shared screen.

## Use speaker view while teaching

Keep both windows and the local server open throughout the lecture. The windows communicate with each other; opening the same deck independently on another device does not create a synchronized speaker view.

| Action | How |
| --- | --- |
| Open speaker view | Focus the main slide window and press `S`. |
| Advance or go back | Use `Right Arrow` / `Left Arrow` in the main slide window. |
| Follow presentation order | Use `Space` or `N` for next; `P` for previous. |
| Show slide overview | Press `Esc` or `O` in the main slide window; select a slide to jump to it. |
| Enter full screen | Press `F` in the main slide window; use `Esc` to exit. |
| View keyboard help | Press `?` in the main slide window. |
| Change the speaker-view arrangement | Use the Layout selector in speaker view. |
| Restart the presentation timer | Click the timer in speaker view. |

The Day 1 deck hides on-slide navigation arrows (`controls: false`), so use keyboard navigation. Shortcuts require focus in the presentation rather than in the browser address bar or another application.

Before teaching, select a speaker-view layout that gives the notes enough space. If the text is too small, enlarge the window or adjust browser zoom in that window. Confirm that notes and slide previews remain readable after changing the layout or zoom.

## Pre-lecture check

- [ ] Start the local server and open `http://127.0.0.1:8000/day1.html`.
- [ ] Confirm the slides render correctly and the CDN is reachable.
- [ ] Press `S`, allow the pop-up, and confirm the first slide's notes appear.
- [ ] Advance and go back once; confirm the notes follow the current slide.
- [ ] Arrange the audience window and private speaker-view window.
- [ ] Check the projected image or meeting preview for accidental notes exposure.
- [ ] Return to the opening slide and reset the timer.
- [ ] Silence notifications and connect laptop power.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Pressing `S` does nothing | Click the main slide area first. Check for a blocked pop-up, allow it for this local address, and press `S` again. The pop-up may also be behind another window. |
| Speaker view reports an origin or connection error | Use the HTTP URL, not `file://`. Close the speaker-view window and reopen it with `S` from the loaded presentation. Keep the same host and port; do not switch between `localhost` and `127.0.0.1` midway. |
| Notes are blank | Check a known slide, such as the opening slide with "Welcome everyone." Confirm you opened the HTML deck, not a PDF. Close speaker view, reload the main deck, then press `S` again. |
| Slides are unstyled or shortcuts do not work | Confirm internet access to `cdn.jsdelivr.net`. The Reveal.js CSS, JavaScript, and notes plugin are loaded from that CDN. |
| Notes stop following the slides | Keep the original main presentation window open. Close the stale speaker-view window and press `S` from the presentation you are actually using. |
| The audience can see notes | Stop sharing immediately. Share only the main presentation window, or turn off display mirroring and move notes to the private display. |
| Terminal reports that port 8000 is already in use | Change `8000` to `8001` in the server command and open `http://127.0.0.1:8001/day1.html`. |
| The browser cannot connect | Confirm that the server command is still running and that the browser URL uses the same port. |

After the lecture, stop sharing, close speaker view, and press `Control+C` in the server's Terminal window to stop the local server.

## Other course days and reference

The Day 2 and Day 3 HTML decks also enable the notes plugin. With the same server running, open `http://127.0.0.1:8000/day2.html` or `http://127.0.0.1:8000/day3.html`, then press `S` from that deck.

Reveal.js reference: [Speaker View](https://revealjs.com/speaker-view/).
