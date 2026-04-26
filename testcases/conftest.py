import pytest
import requests
import allure
from common.config import BASE_URL, HEADERS, LOGIN_DATA

@pytest.fixture(scope="session")
def token():
    response = requests.post(
        url = f"{BASE_URL}/api/v1/auth/login",
        headers=HEADERS,
        json=LOGIN_DATA
    )
    resp_json = response.json()
    _token = resp_json.get("access_token")
    assert _token != "", f"获取token失败，响应：{resp_json}"
    return _token

@pytest.fixture(scope="session")
def auth_headers(token):
    """返回带token的请求头，所有需要登录的用例直接用这个"""
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {token}"
    return headers