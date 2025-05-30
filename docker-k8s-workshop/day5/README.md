# 2-Tier Kubernetes Application with Helm (Day 5)

## Components
- Frontend + Backend (Python Flask)
- Horizontal Pod Autoscaler (CPU-based)
- Liveness and Readiness Probes
- Resource Limits for cost and performance control

## Performance & Cost Optimizations
- Probes help avoid unresponsive pods affecting UX.
- Resource limits prevent noisy neighbor issues and optimize cluster usage.
- HPA handles traffic surges like flash sales or seasonal spikes efficiently.

## Core Concept Questions

### 1. Why are liveness and readiness probes critical in keeping a product’s user experience stable and reliable?

Liveness and readiness probes are critical in Kubernetes because they help maintain application health and availability, which directly impacts the user experience:

1. Liveness Probe ensures the app is still running. If it fails, Kubernetes restarts the container automatically, avoiding stuck or unresponsive services.

2. Readiness Probe ensures the app is ready to handle traffic. It prevents users from reaching the app until it's fully initialized, avoiding errors or failed requests.

Together, they ensure users always interact with healthy, responsive instances, improving stability and reliability.

### How does HPA help in handling flash sales, seasonal load spikes, or traffic surges in real-world applications like an e-commerce platform?

Horizontal Pod Autoscaler (HPA) helps real-world applications like e-commerce platforms handle flash sales, seasonal spikes, or sudden traffic surges by:

1. Automatically increasing the number of pods based on real-time CPU/memory usage or custom metrics like request rate.

2. Ensuring high availability and performance during peak traffic.

3. Scaling down during low demand to optimize costs.

This dynamic scaling keeps the app responsive and avoids crashes, providing a smooth experience for all users.
