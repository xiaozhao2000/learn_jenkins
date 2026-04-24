import pytest
import requests


from common.config import BASE_URL, HEADERS, LOGIN_DATA, CHECK_VERSION_DATA



class TestLogin:
    """登录接口测试"""

    def test_login_success(self):
        """正常登录，验证返回token"""
        response = requests.post(
            url=f"{BASE_URL}/api/v1/auth/login",
            headers=HEADERS,
            json=LOGIN_DATA
        )

        print(f"\n登录响应：{response.json()}")

        assert response.status_code == 200, f"状态码错误：{response.status_code}"

        resp_json = response.json()
        assert "token" in str(resp_json).lower() or "access" in str(resp_json).lower(), \
            f"响应中未找到token：{resp_json}"
