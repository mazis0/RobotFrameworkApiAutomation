import requests

class UserApiPage:

    BASE_URL = "https://reqres.in/api"

    def get_single_user(self, user_id):
        return requests.get(f"{self.BASE_URL}/users/{user_id}")

    def create_user(self, email, password):
        headers = {
            "Content-Type": "application/json",
            "x-api-key": "reqres-free-v1"
        }
        payload = {"email": email, "password": password}
        return requests.post(f"{self.BASE_URL}/register",
                             json=payload,
                             headers=headers)