🐳 Python Docker App

This is a simple Python application containerized using Docker.
The project helps beginners understand how to create a Docker image and run a Python app inside a container.

python-docker/
│
├── Dockerfile
├── app.py
├── requirements.txt   (optional)
└── README.md

🛠 Prerequisites

• Make sure you have the following installed:

• Docker

• Python (optional, only for local testing)

 • Linux / WSL / macOS / Windows

🐍 Pyhtonfile

import qrcode

url = input("enter your URL = ").strip()
file_path = "C:\\Users\\acer\\OneDrive\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

img.show()

print("QR CODE HAS DONE")

📄 Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install flask

CMD ["python", "app.py"]

🚀 How to Build Docker Image

Run this command inside the project directory (where Dockerfile exists):

docker build -t python-app .
