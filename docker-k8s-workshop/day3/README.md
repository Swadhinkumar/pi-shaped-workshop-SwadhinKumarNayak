# Day 3 - Exposing App Using Ingress in Kubernetes
This project demonstrates how to expose a Flask-based Docker app in a Minikube Kubernetes environment using Ingress, with service types like ClusterIP and optionally NodePort.

Prerequisites
Minikube installed and started
kubectl configured for Minikube
Docker installed
Minikube ingress addon enabled:
minikube addons enable ingress

# Step 1: Clone the Repo
git clone https://github.com/Swadhinkumar/pi-shaped-workshop-SwadhinKumarNayak.git
cd pi-shaped-workshop-SwadhinKumarNayak/docker-k8s-workshop/day3
# Step 2: Apply Deployment & Service
kubectl apply -f deployment.yaml
kubectl apply -f clusterip-service.yaml
# Step 3: Apply Ingress Recource
kubectl apply -f ingress.yaml
# Step 4: Update /etc/hosts for Domain Resolution
sudo nano /etc/hosts
192.168.49.2 flask-hello.local //Add this line at the end:
# Step 5: Access the App
Now open your browser and go to: http://flask-hello.local/hello

# Core Concept Questions
1. How would you expose an internal microservice (e.g., user-auth) differently than a public-facing frontend in a Kubernetes-based product?
For internal microservices like user-auth, we use ClusterIP service to make them accessible only within the cluster. This ensures security and keeps internal logic isolated.

For public-facing frontends, we use Ingress or LoadBalancer to expose the services to users outside the cluster.

2. Why might a product use Ingress instead of directly exposing each microservice via LoadBalancer?
Ingress allows routing multiple services via a single IP address with path-based or host-based routing, reducing cost and simplifying DNS management. Using one LoadBalancer per service is costly and complex, while Ingress is scalable and efficient.
