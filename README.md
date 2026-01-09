🐍 Python App On Docker
A beginner-friendly project showing how to containerize a simple Python application using Docker.
Learn how to write a Dockerfile, build a Docker image, and run your Python app inside a container. �
GitHub


🧾 Table of Contents

📋 About

📁 Project Structure

🚀 Prerequisites

🛠️ Dockerfile Explained

📦 Build Docker Image

▶️ Run Docker Container

📝 Notes

📌 License


📋 About
This repository demonstrates how to package a Python script into a Docker image. It’s useful for beginners who are learning how Docker works with Python applications. �
GitHub


📁 Project Structure
Copy code

Python.app-On-Docker/
├── Dockerfile
├── README.md
└── qr code.py

Dockerfile – Instructions to build the Docker image.

qr code.py – Python script that generates a QR code.

README.md – This file. �

GitHub


🚀 Prerequisites

Make sure you have the following installed:


🐳 Docker — Install Docker Desktop or Docker 
Engine



🐍 Python (optional — only for local testing)


🛠️ Dockerfile Explained

Your Dockerfile sets up the image to run the Python app inside a container:

Copy code

Dockerfile

FROM python:3.12-slim

WORKDIR /app

COPY src/main.python /app/main.python

RUN pythonc src/main.python

CMD ["python","main"]


What it does:

Uses the base image python:3.12-slim

Sets the working directory to /app

Copies your Python script into the container

(Optional) Compiles the code

Starts the Python app when the container runs

You may want to rename src/main.python → 

app.py for a standard Python filename. �

GitHub


📦 Build Docker Image

Navigate to the root directory (where your 

Dockerfile is located), then run:

Copy code

Sh

docker build -t python-app .

This creates a Docker image named python-app. �

GitHub


▶️ Run Docker Container

Once the image is built, start the container:

Copy code

Sh

docker run python-app

This will execute your Python script inside 
the container. �

GitHub


📝 Notes

✔️ Make sure paths in the Dockerfile match the actual folder structure.

✔️ Rename files to .py if the extension is nonstandard.

✔️ You can add a requirements.txt to install extra packages with pip. �
GitHub


📌 License

This project currently has no license specified.
