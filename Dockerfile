FROM python:3.12-slim

WORKDIR /app

COPY src/main.python /app/main.python

RUN pythonc src/main.python

CMD ["python","main"]
