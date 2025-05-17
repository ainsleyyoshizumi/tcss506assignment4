#!/bin/bash
echo "Building Docker image"
docker build -t flask-app .

echo "Running the Docker container..."
docker run -d -p 5000:5000 --name flask-app-container flask-app

echo "Docker contianer is running. Use 'docker ps' to check the status."