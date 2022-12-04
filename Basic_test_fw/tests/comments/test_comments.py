import pytest
import requests
from lib.utils import build_request_headers
from lib.comments import Comments

def test_get_all_comments(login_as_admin):
   response = Comments().get_all_comments("http://10.78.213.212:8080", login_as_admin)
   assert response.ok

