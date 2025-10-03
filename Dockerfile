FROM python:3.8-slim-buster

# Install system dependencies and AWS CLI
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        awscli \
        curl \
        unzip \
        git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python", "app.py"]
