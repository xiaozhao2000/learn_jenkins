import requests


from common.config import BASE_URL, HEADERS, LOGIN_DATA, CHECK_VERSION_DATA

def login_success():
    """正常登录，验证返回token"""
    response = requests.post(
        url=f"{BASE_URL}/api/v1/auth/login",
        headers=HEADERS,
        json=LOGIN_DATA
    )
    print(response.status_code)
    print("响应体:", response.json())
    print(type(response.json()))
    print(response.json().get("access_token"))
login_success()
