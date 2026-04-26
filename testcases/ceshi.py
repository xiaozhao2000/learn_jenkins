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

import pytest
import requests
import allure
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.config import BASE_URL, HEADERS, CHECK_VERSION_DATA


@allure.feature("版本检查模块")
class TestCheckVersion:

    @allure.story("正常检查版本")
    @allure.title("携带有效token检查版本，验证返回结果")
    @allure.severity(allure.severity_level.NORMAL)
    def test_check_version(self, auth_headers):
        """auth_headers 直接从 conftest.py 注入，不需要自己登录"""
        with allure.step("发送检查版本请求"):
            response = requests.post(
                url=f"{BASE_URL}/api/v1/ota/check_version",
                headers=auth_headers,
                json=CHECK_VERSION_DATA
            )

        with allure.step("验证状态码为200"):
            assert response.status_code == 200, f"状态码错误：{response.status_code}"

        with allure.step("验证响应不为空"):
            resp_json = response.json()
            print(f"\n检查版本响应：{resp_json}")
            assert resp_json is not None, "响应为空"

    @allure.story("异常场景")
    @allure.title("不携带token检查版本，验证返回401或403")
    @allure.severity(allure.severity_level.NORMAL)
    def test_check_version_without_token(self):
        with allure.step("发送不带token的请求"):
            response = requests.post(
                url=f"{BASE_URL}/api/v1/ota/check_version",
                headers=HEADERS,
                json=CHECK_VERSION_DATA
            )

        with allure.step("验证状态码为401或403"):
            print(f"\n无token响应：{response.json()}")
            assert response.status_code in [401, 403], \
                f"未授权请求应返回401或403，实际返回：{response.status_code}"