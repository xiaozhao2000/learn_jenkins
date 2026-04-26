import allure
import pytest
import requests

from common.config import BASE_URL, HEADERS, LOGIN_DATA, CHECK_VERSION_DATA


@allure.feature("检查版本模块")
class TestCheckVersion:
    """检查版本接口测试"""

    @allure.story("正常检查版本信息")
    @allure.title("使用access_token获取版本信息")
    def test_check_version(self, auth_headers):
        """检查版本，验证返回结果"""
        with allure.step("使用配置文件中的信息发送请求"):
            response = requests.post(
                url=f"{BASE_URL}/api/v1/ota/check_version",
                headers=auth_headers,
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
