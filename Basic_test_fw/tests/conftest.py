import pytest
from config import SESSION, APP_URL, ADMIN_USER, ADMIN_PASSWORD

@pytest.fixture(scope="session")
def login_as_admin():
    # 1 - Auth
   payload = {'username': ADMIN_USER, 'password': ADMIN_PASSWORD}
   response = SESSION.post(f'{APP_URL}/auth/login', data=payload)
   assert response.ok

   # 2 - Get comments
   access_token = response.json()["access_token"]
   yield access_token