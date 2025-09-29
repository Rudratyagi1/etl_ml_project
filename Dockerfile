# Use a supported base image
FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies (optional — add only if you need them)
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
       curl unzip \
    && rm -rf /var/lib/apt/lists/*

# Install AWS CLI via pip (lighter than apt)
RUN pip install --no-cache-dir awscli

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command (update if your app entrypoint differs)
CMD ["python", "main.py"]
