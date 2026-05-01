# Docker Nginx Project 🚀

This project demonstrates containerizing a static web application using Docker.

## Features
- Custom HTML page served via Nginx
- Dockerfile for building image
- Versioning (v1, v2)
- Port mapping (8080, 8081)

## How to Run

Build image:
docker build -t sree-nginx:v1 .

Run container:
docker run -d -p 8080:80 sree-nginx:v1

Access:
http://localhost:8080

## Author
Sreenidhi
