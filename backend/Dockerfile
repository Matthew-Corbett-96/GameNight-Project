# Use an official Python runtime as a parent image
FROM python:3.12.1-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y gcc

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN /bin/bash -c "pip install --no-cache-dir -r requirements.txt"

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8000 available for the app
EXPOSE 8000
