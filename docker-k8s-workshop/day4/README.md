# Flask Hello App - Helm Chart (Day 4)
## Overview
This is a Helm chart for deploying the simple Flask Hello app. It allows configuration of image, port, and replica count.

## How to Use

### 1. Clone the repository
git clone https://github.com/yourusername/pi-shaped-workshop-SwadhinKumarNayak.git
cd pi-shaped-workshop-SwadhinKumarNayak/docker-k8s-workshop/day4/

### 2: Install the Helm chart
helm install flask-hello ./flask-hello
### 3: Update /etc/hosts for Domain Resolution
sudo nano /etc/hosts
192.168.49.2 flask-hello.local //Add this line at the end:

### 4: Access the App
Now open your browser and go to: http://flask-hello.local/hello

### 5: Uninstall the release
helm uninstall flask-hello

## Core Concept Questions

### 1. Why is Helm important for managing configuration across different environments in a real-world product (e.g., dev, staging, prod)?
Helm is important because it allows you to templatize Kubernetes manifests, making it easy to manage configuration differences across environments like dev, staging, and prod. You can reuse the same chart and customize values using separate values.yaml files, ensuring consistency, reducing duplication, and simplifying deployment.

### 2. How does Helm simplify deployment rollback during a production incident?
Helm simplifies deployment rollback by maintaining a history of all releases. If something goes wrong in production, you can easily revert to a previous stable version using a single command like helm rollback. This reduces downtime and ensures quick recovery without manually changing YAML files.
