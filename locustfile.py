from locust import HttpUser, task, constant

class HelloWorldUser(HttpUser):
    host = "http://localhost:8000" 
    wait_time = constant(1)
    
    @task
    def hello_world(self):
        self.client.get("/")