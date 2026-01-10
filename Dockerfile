FROM python:3.12-slim

WORKDIR /app

COPY SRC/qr code.py /app/qr code.py

CMD ["python","qr code.py"]
