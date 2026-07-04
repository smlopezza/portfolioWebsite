# syntax=docker/dockerfile:1

FROM python:3.10-slim

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# git is required at import time by GitPython (used in app/routes.py),
# even though the route that uses it isn't exercised on Cloud Run.
# Without it, `import git` raises ImportError and the container fails to start.
RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
    && rm -rf /var/lib/apt/lists/*
 
# Install Python deps first for better layer caching
# (requirements.txt already includes gunicorn)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the rest of the app
COPY . .
 
# Cloud Run injects PORT (defaults to 8080). Gunicorn must bind to it.
ENV PORT=8080
EXPOSE 8080
 
# application.py does `from app import app`, so the WSGI target is application:app
CMD exec gunicorn --bind :${PORT} --workers 1 --threads 8 --timeout 0 application:app