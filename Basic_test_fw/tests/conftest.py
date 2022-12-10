import pytest
from config import SESSION, APP_URL, ADMIN_USER, ADMIN_PASSWORD, LOG

@pytest.fixture(scope="session")
def login_as_admin():
    LOG.info("login_as_admin()")
    # 1 - Auth
    payload = {'username': ADMIN_USER, 'password': ADMIN_PASSWORD}
    LOG.debug(f'Loging payload: {payload}')
    response = SESSION.post(f'{APP_URL}/auth/login', data=payload)
    assert response.ok

    # 2 - Get comments
    access_token = response.json()["access_token"]
    yield access_token