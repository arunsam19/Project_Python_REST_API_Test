import pytest
import requests

@pytest.fixture(scope="session")
def login_as_admin():
    # 1 - Auth
   payload = {'username': 'admin', 'password': 'admin'}
   response = requests.post("http://10.78.213.212:8080/auth/login", data=payload)
   assert response.ok

   # 2 - Get comments
   access_token = response.json()["access_token"]
   yield access_token