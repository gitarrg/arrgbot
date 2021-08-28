FROM python:3.8-slim

# DEPS
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt


ENV PYTHONPATH /app

#### CODE
COPY . /app/arrgbot

#### MAIN
WORKDIR /app
CMD ["python", "/app/arrgbot/main.py"]

