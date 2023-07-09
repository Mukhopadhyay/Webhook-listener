import os
from celery import Celery
from datetime import datetime

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
app = Celery(__name__, broker=redis_url, backend=redis_url)


@app.task
def dummy_task():
    folder = "./tmp/celery"
    os.makedirs(folder, exist_ok=True)
    now = datetime.now().isoformat()
    with open(f"{folder}/task-{now}.txt", "w") as f:
        f.write(f"hello @ {now}")
