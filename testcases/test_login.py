import allure
import pytest
import requests


from common.config import BASE_URL, HEADERS, LOGIN_DATA, CHECK_VERSION_DATA


@allure.feature("登录模块")
class TestLogin:
    """登录接口测试"""
    @allure.story("正常登录")
    @allure.title("使用正确邮箱密码")
    def test_login_success(self):
        """正常登录，验证返回token"""
        with allure.step("使用配置文件中的信息发送请求"):
            response = requests.post(
                url=f"{BASE_URL}/api/v1/auth/login",
                headers=HEADERS,
                json=LOGIN_DATA
            )
        with allure.step("验证状态码是否等于200"):
            assert response.status_code == 200, f"状态码错误：{response.status_code}"

        with allure.step("验证响应中是否包含access_token"):
            resp_json = response.json()
            assert "token" in str(resp_json).lower() or "access" in str(resp_json).lower(), \
                f"响应中未找到token：{resp_json}"
