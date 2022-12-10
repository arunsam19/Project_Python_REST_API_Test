import pytest
import requests

def test_health():
    resp = requests.get("http://10.78.213.212:8080/health")
    assert resp.ok