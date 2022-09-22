# FROM python:3
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /app
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install -r requirements.txt
# COPY . /app/
# syntax=docker/dockerfile:1
FROM python:3.6-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/