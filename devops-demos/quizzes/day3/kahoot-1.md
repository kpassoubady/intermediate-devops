# Day 3 Section Quiz 1: Kubernetes

Placement: immediately before "Lab 08: Kubernetes deployments, rollouts and rollbacks".
Budget: 5 minutes, including joining and debrief. Answer time: 20 seconds per question.
Scope: preceding Day 3 containers and Kubernetes teaching plus completed Lab 07.
Instructor-only answer key. Offer A/B/C/D in chat, a private note, or passing as alternatives to Kahoot.

## Q1 (MCQ)

Question: A Pod's readiness probe fails. What happens?

- A: It stops receiving Service traffic without a probe-triggered restart
- B: Its container restarts after the readiness failure threshold
- C: Its Deployment rolls back to the previous ReplicaSet
- D: Its scheduler moves it to another node

Correct Answer: A
Explanation: Readiness controls whether the Pod receives Service traffic. Liveness failures can trigger restarts.
Grounding: `../../slides/day3.html`, "Liveness, readiness and startup probes".

## Q2 (MCQ)

Question: A Deployment wants three Pods, but one is deleted. Why does a replacement appear?

- A: The Service creates a Pod for each missing endpoint
- B: The deleted Pod restarts itself on another node
- C: A controller reconciles the actual count with the desired count
- D: The Ingress retries the failed Pod's image

Correct Answer: C
Explanation: The ReplicaSet controller notices the shortfall and creates a Pod to restore the desired count.
Grounding: `../../slides/day3.html`, "The declarative API and reconciliation loops".

## Q3 (MCQ)

Question: What happens when a container tries to use more CPU than its configured CPU limit?

- A: Its Pod is evicted as soon as the limit is reached
- B: Its container is killed for exceeding the limit
- C: Its scheduler increases the CPU request
- D: Its CPU use is throttled

Correct Answer: D
Explanation: CPU limits throttle usage; exceeding a memory limit can kill the container.
Grounding: `../../slides/day3.html`, "Requests, limits and quality of service".

## Q4 (True/False)

Question: A Service provides a stable name and address for a changing set of Pods.

- A: True
- B: False

Correct Answer: A (True)
Explanation: A Service provides a stable endpoint while the Pods behind it can change.
Grounding: `../../slides/day3.html`, "Services and Ingress".
