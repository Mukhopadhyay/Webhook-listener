#!/bin/bash

set -e

# Wait
sleep 5

WORKERS=${WORKERS:-1}
LOG_LEVEL=${LOG_LEVEL:-INFO}

usage() {
    echo "Usage: $0 [celery|fastapi]"
    echo "  - fastapi: Start the fastapi server"
    echo "  - celery: Start the celery worker"
}

if [[ "$1" == "celery" ]]; then
    celery --app=tasks.celery_app.app worker --concurrency=$WORKERS --loglevel=$LOG_LEVEL
elif [[ "$1" == "fastapi" ]]; then
    # Change this to Gunicorn based on the ENV var
    python3 -m uvicorn app.app:app --port 8000 --host 0.0.0.0 --reload
else
    echo "Unknown or missing sub-command: '$1'"
    usage
    exit 1
fi

