#!/bin/bash

set -e

# Wait
sleep 5

WORKERS=${WORKERS:-1}
PORT=${PORT:-8000}
LOG_LEVEL=${LOG_LEVEL:-INFO}
MODE=${MODE:-development}

usage() {
    echo "Usage: $0 [celery|fastapi]"
    echo "  - fastapi: Start the fastapi server"
    echo "  - celery: Start the celery worker"
}

if [[ "$1" == "celery" ]]; then
    celery --app=tasks.celery_app.app worker --concurrency=$WORKERS --loglevel=$LOG_LEVEL
elif [[ "$1" == "fastapi" ]]; then
    echo "Running in '$MODE' mode"
    if [[ $MODE == "development" ]]; then
        # Change this to Gunicorn based on the ENV var
        python3 -m uvicorn app.app:app --port $PORT --host 0.0.0.0 --reload
    elif [[ $MODE == "production" ]]; then
        python3 -m gunicorn --worker-class uvicorn.workers.UvicornWorker --bind "0.0.0.0:${PORT}" -w $WORKERS app.app:app --log-level $LOG_LEVEL
    fi
else
    echo "Unknown or missing sub-command: '$1'"
    usage
    exit 1
fi
