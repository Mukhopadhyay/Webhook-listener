#!/bin/sh

# Wait
sleep 5

# Starting the FastAPI server
echo "Webhook startup"
python3 -m uvicorn app:app --port 8000 --host 0.0.0.0 --reload
