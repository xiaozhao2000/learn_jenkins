import allure
import pytest
import requests

from common.config import BASE_URL, HEADERS, LOGIN_DATA, CHECK_VERSION_DATA


@allure.feature("检查版本模块")
class TestCheckVersion:
    """检查版本接口测试"""

    @pytest.fixture
    @allure.title("获取access_token")
    def access_token(self):
        """登录并返回 access_token，供需要鉴权的用例显式使用。"""
        response = requests.post(
            url=f"{BASE_URL}/api/v1/auth/login",
            headers=HEADERS,
            json=LOGIN_DATA
        )

        assert response.status_code == 200, f"登录状态码错误：{response.status_code}"

        resp_json = response.json()
        access_token = resp_json.get("access_token")
        assert access_token, f"获取 access_token 失败，响应：{resp_json}"
        return access_token

    @allure.story("正常检查版本信息")
    @allure.title("使用access_token获取版本信息")
    def test_check_version(self, access_token):
        """检查版本，验证返回结果"""
        with allure.step("copy配置中的请求头，添加token"):
            headers = HEADERS.copy()
            headers["Authorization"] = f"Bearer {access_token}"
        with allure.step("使用配置文件中的信息发送请求"):
            response = requests.post(
                url=f"{BASE_URL}/api/v1/ota/check_version",
                headers=headers,
                json=CHECK_VERSION_DATA
            )
        with allure.step("验证状态码是否为200"):
            assert response.status_code == 200, f"状态码错误：{response.status_code}"
        with allure.step("验证响应内容不为空"):
            resp_json = response.json()
            assert resp_json is not None, "响应为空"
    @allure.story("异常检查版本信息的场景")
    @allure.title("不带token获取版本信息")
    def test_check_version_without_token(self):
        """不带token请求，验证返回401或403"""
        with allure.step("发送请求，不带token"):
            response = requests.post(
                url=f"{BASE_URL}/api/v1/ota/check_version",
                headers=HEADERS,
                json=CHECK_VERSION_DATA
            )

        with allure.step("验证接口处理异常场景，返回401或者403"):
            assert response.status_code in [401, 403], \
                f"未授权请求应返回401或403，实际返回：{response.status_code}"
