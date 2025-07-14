from locust import HttpUser, task

class CountUser(HttpUser):
    @task
    def increment_count(self):
        self.client.get("/count")
