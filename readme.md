# Docker Volume Upgrade Project

## 🚀 Overview

This project demonstrates a multi-container Dockerized application with persistent storage using Docker Volumes.

Architecture:

Browser → Nginx → Flask Backend → Docker Volume

---

## 🧠 Features

- Multi-container architecture
- Docker Compose orchestration
- Flask backend
- Nginx reverse proxy
- Persistent storage using Docker Volumes
- Stateful containerized application

---

## 📦 Technologies Used

- Docker
- Docker Compose
- Flask
- Nginx
- Python

---

## 🚀 Project Structure

static-site1/
│
├── backend/
│   ├── app.py
│   └── Dockerfile
│
├── docker-compose.yml
│
└── README.md

---

## 🚀 Run The Project

```bash
docker-compose up --build
