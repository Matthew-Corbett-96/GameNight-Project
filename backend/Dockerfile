# Use an official Python runtime as a parent image
FROM python:3.11.3-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN /bin/bash -c "pip install --no-cache-dir -r requirements.txt"

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available for the app
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
