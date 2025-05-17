#!/bin/bash
echo "Building Docker image..."
docker build -t flask-app .

echo "Stopping and removing any existing container..."
docker stop flask-app-container 2>/dev/null
docker rm flask-app-container 2>/dev/null

echo "Running Docker container on port 5000..."
docker run -d -p 5000:5000 --name flask-app-container flask-app

echo "App is running! Access it from: http://<EC2_PUBLIC_IP>:5000 (after opening port in security group)"