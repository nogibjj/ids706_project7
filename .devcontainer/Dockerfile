# .devcontainer/Dockerfile
FROM python:3.8

# Configure the environment
ENV PYTHONUNBUFFERED 1

# Install any necessary dependencies
RUN apt-get update && apt-get install -y \
    build-essential

# Set the working directory
WORKDIR /workspace

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
