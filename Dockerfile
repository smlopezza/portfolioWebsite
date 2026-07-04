# syntax=docker/dockerfile:1

FROM python:3.10-slim

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (kept minimal; add build-essential back if any pip package needs compiling)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Cloud Run injects PORT (defaults to 8080). Gunicorn must bind to it.
ENV PORT=8080
EXPOSE 8080

# application.py does `from app import app`, so the WSGI target is application:app
CMD exec gunicorn --bind :${PORT} --workers 1 --threads 8 --timeout 0 application:app