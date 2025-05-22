# Docker Day 1 Exercise 

## Overview
This project is a simple Flask-based "Hello, World!" REST API, containerized using Docker.

## How to Run

```bash
git clone <URL>
cd <repo-name>/docker-k8s-workshop/day1/
docker build -t <image-name>:day1 .
docker run -p 8080:8080 <image-name>:day1
```

## Docker Hub image
[View on Docker Hub]https://hub.docker.com/r/swadhin7008/hello-python


## Core Concept Questions

### 1. Why is Docker useful in building and deploying microservices for a real-world product (like an e-commerce or banking app)?

Docker allows each microservice to be packaged with its own dependencies, libraries, and runtime environment. This ensures that services run consistently across development, testing, and production environments. In a real-world application like e-commerce or banking, where different services (e.g., payments, user auth, product catalog) need to scale and update independently, Docker enables quick deployments, isolation, portability, and easier troubleshooting.

---

### 2. What is the difference between a Docker image and a container in the context of scaling a web application?

A Docker image is a read-only template that contains the application code, dependencies, and configurations.

A Docker container is a running instance of that image.

In terms of scaling, you scale containers, not images. You can launch multiple containers from the same image to handle higher traffic without duplicating the image itself. 

---

### 3. How does Kubernetes complement Docker when running a product at scale (e.g., hundreds of containers)?

Kubernetes is an orchestration tool that automates deployment, scaling, load balancing, and self-healing of containers. While Docker handles containerization, Kubernetes handles how and where those containers run. For large-scale products, Kubernetes ensures:

Containers are distributed across nodes efficiently.

Services can scale up/down based on traffic.

Failed containers are restarted or replaced automatically.

Configuration and secrets are managed securely.


Together, Docker and Kubernetes form a powerful combination for modern cloud-native applications.
