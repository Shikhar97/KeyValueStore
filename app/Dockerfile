# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the requirements.txt
COPY requirements.txt /app/requirements.txt

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the contents of the local app directory into the container at /app
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Uvicorn server and Huey consumer
CMD ["/bin/bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & python3 huey_consumer.py redis_huey.huey -v"]