# Use newer Debian base to avoid 404 errors
FROM python:3.10-slim-bullseye

WORKDIR /app
COPY . /app

# Install dependencies and AWS CLI via pip
RUN apt-get update -y && \
    apt-get install -y unzip jq curl && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir awscli && \
    rm -rf /var/lib/apt/lists/*

CMD ["python3", "app.py"]
