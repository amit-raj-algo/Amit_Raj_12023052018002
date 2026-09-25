import requests


class APIClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_post(self, post_id):
        return requests.get(
            f"{self.BASE_URL}/posts/{post_id}"
        )

    def create_post(self, payload):
        return requests.post(
            f"{self.BASE_URL}/posts",
            json=payload
        )