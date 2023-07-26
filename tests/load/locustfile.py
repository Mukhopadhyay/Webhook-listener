"""
Locustfile
**********
Locustfile is the init point for the Locust load testing framework. Read more about writing
tests here, https://docs.locust.io/en/stable/writing-a-locustfile.html

>> locust -f locustfile.py -H http://localhost:9000
"""

from locust import HttpUser, task, between


class WebhookUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_non_celery_endpoint(self):
        body = {"message": "Locust request", "delay": 3}
        self.client.post("/v1/listener1/nonCelery/", json=body)

    @task
    def test_celery_endpoint(self):
        body = {"message": "Locust request", "delay": 3}
        self.client.post("/v1/listener1/", json=body)
