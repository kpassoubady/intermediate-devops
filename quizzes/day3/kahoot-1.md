# Day 3 Section Quiz 1: Kubernetes

Placement: immediately before "Lab 08: Kubernetes deployments, rollouts and rollbacks".
Budget: 5 minutes, including joining and debrief. Answer time: 20 seconds per question.
Scope: preceding Day 3 containers and Kubernetes teaching plus completed Lab 07.
Instructor-only answer key. Offer A/B/C/D in chat, a private note, or passing as alternatives to Kahoot.

## Q1 (MCQ)

Question: A Pod's readiness probe fails. What happens?

- A: It stops receiving Service traffic without a probe-triggered restart
- B: The container image is permanently deleted from the registry
- C: Its Deployment rolls back to the initial commit in git
- D: The ReplicaSet scales down to zero replicas immediately

Correct Answer: A
Explanation: Readiness controls whether the Pod receives Service traffic. Liveness failures can trigger restarts.
Grounding: `../../slides/day3.html`, "Liveness, readiness and startup probes".

## Q2 (MCQ)

Question: A Deployment wants three Pods, but one is deleted. Why does a replacement appear?

- A: An external load balancer compiles a new application binary
- B: The container registry pushes a new image tag automatically
- C: A controller reconciles the actual count with the desired count
- D: The web browser requests a replacement pod from git

Correct Answer: C
Explanation: The ReplicaSet controller notices the shortfall and creates a Pod to restore the desired count.
Grounding: `../../slides/day3.html`, "The declarative API and reconciliation loops".

## Q3 (MCQ)

Question: What happens when a container tries to use more CPU than its configured CPU limit?

- A: The host node deletes the container's source code
- B: The container is granted unlimited root CPU priority
- C: The Kubernetes scheduler restarts all nodes in the cluster
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

## Q5 (MCQ)

Question: What Linux kernel feature isolates what a container process can see?

- A: Cron scheduled jobs
- B: Linux namespaces
- C: Bash shell history files
- D: The system clock time zone

Correct Answer: B
Explanation: Namespaces isolate visibility (process IDs, network interfaces, mounts, and hostnames).
Grounding: `../../slides/day3.html`, "Linux namespaces isolate what a process can see".

## Q6 (MCQ)

Question: What happens when a container exceeds its configured memory limit?

- A: The container's disk drive is permanently formatted
- B: The kernel Out-Of-Memory (OOM) killer terminates the process
- C: The cluster re-compiles the application source code
- D: The container creates a new git branch

Correct Answer: B
Explanation: Unlike CPU which is throttled, exceeding memory limits triggers the Linux OOM killer to terminate the container.
Grounding: `../../slides/day3.html`, "Requests, limits and quality of service".

## Q7 (MCQ)

Question: Why are multi-stage Docker builds recommended for production images?

- A: They automatically run the container on multiple operating systems
- B: They keep images small and exclude compilers and build tools
- C: They store source code and passwords inside the public image
- D: They prevent containers from using network connections

Correct Answer: B
Explanation: Multi-stage builds copy only compiled artifacts into a minimal runtime image, reducing image size and attack surface.
Grounding: `../../slides/day3.html`, "Dockerfile practices".

## Q8 (MCQ)

Question: Why is referencing an image by sha256 digest safer than using a tag?

- A: Image tags can never be viewed by users
- B: A digest is an immutable cryptographic hash of image content
- C: Digests make container images run ten times faster
- D: Digests automatically encrypt all network traffic

Correct Answer: B
Explanation: Image tags can be overwritten or moved; an image digest is an immutable cryptographic hash of the content.
Grounding: `../../slides/day3.html`, "Tags and digests".

## Q9 (MCQ)

Question: Which Kubernetes component serves as the persistent store for cluster state?

- A: An ephemeral cache in container memory
- B: etcd
- C: Temporary command-line bash history
- D: An uncommitted text file on a local workstation

Correct Answer: B
Explanation: etcd is the consistent, highly-available key-value store used as Kubernetes' backing store for all cluster data.
Grounding: `../../slides/day3.html`, "The control plane and the nodes".

## Q10 (True/False)

Question: Unlike virtual machines, containers share the host operating system kernel.

- A: True
- B: False

Correct Answer: A (True)
Explanation: Containers share the underlying Linux kernel with the host and other containers, while VMs run separate guest OS kernels.
Grounding: `../../slides/day3.html`, "Virtual machines and containers".

## Q11 (MCQ)

Question: In AWS ECS, which serverless engine runs tasks without managing EC2 instances?

- A: AWS S3 Glacier Tape Archive
- B: AWS Fargate
- C: Amazon Route 53 DNS records
- D: AWS Simple Email Service (SES)

Correct Answer: B
Explanation: AWS Fargate is a serverless compute engine for containers that removes the need to provision or manage EC2 instances.
Grounding: `../../slides/day3.html`, "Fargate runs tasks without servers to manage".

## Q12 (True/False)

Question: A liveness probe failure in Kubernetes causes kubelet to restart the container.

- A: True
- B: False

Correct Answer: A (True)
Explanation: When a liveness probe fails past its threshold, the kubelet kills and restarts the container to recover from deadlocks.
Grounding: `../../slides/day3.html`, "Liveness, readiness and startup probes".
