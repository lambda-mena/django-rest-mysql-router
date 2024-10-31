from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class TestAuth(APITestCase):
    endpoint_url = "/api/auth/sign-up/"
    databases = ["test"]

    def test_return_user_tokens(self):
        new_credentials = {"username": "test", "password": "Aax123456"}
        response = self.client.post(self.endpoint_url, new_credentials)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
