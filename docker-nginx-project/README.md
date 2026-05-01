# Docker Nginx Project 🚀

This project demonstrates containerizing a static web application using Docker and Nginx.

## Features
- Custom HTML page served via Nginx
- Docker image creation using Dockerfile
- Container deployment with port mapping
- Versioning support (v1, v2)

## How to Run

Build image:
docker build -t sree-nginx .

Run container:
docker run -d -p 8080:80 sree-nginx

Access:
http://localhost:8080

## Tech Stack
- Docker
- Nginx
- Linux (WSL)

## Author
Sreenidhi
