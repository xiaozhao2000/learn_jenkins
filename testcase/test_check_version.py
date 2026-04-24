from common.config import BASE_URL, HEADERS, LOGIN_DATA, CHECK_VERSION_DATA

import pytest
import requests


class TestCheckVersion:
    """检查版本接口测试"""

    @pytest.fixture(autouse=True)
    def get_token(self):
        """每个用例执行前先登录获取token"""
        response = requests.post(
            url=f"{BASE_URL}/api/v1/auth/login",
            headers=HEADERS,
            json=LOGIN_DATA
        )
        resp_json = response.json()
        print(f"access_token：{resp_json.get('access_token')}")

        # 从响应中提取token，先告诉我登录成功后返回的数据结构
        # 暂时用占位，等你告诉我返回结构后修改
        self.token = resp_json.get("access_token", {})
        assert self.token != "", f"获取token失败，响应：{resp_json}"

    def test_check_version(self):
        """检查版本，验证返回结果"""
        headers = HEADERS.copy()
        headers["Authorization"] = f"Bearer {self.token}"

        response = requests.post(
            url=f"{BASE_URL}/api/v1/ota/check_version",
            headers=headers,
            json=CHECK_VERSION_DATA
        )

        print(f"\n检查版本响应：{response.json()}")

        assert response.status_code == 200, f"状态码错误：{response.status_code}"

        resp_json = response.json()
        assert resp_json is not None, "响应为空"


    def test_check_version_without_token(self):
        """不带token请求，验证返回401或403"""
        response = requests.post(
            url=f"{BASE_URL}/api/v1/ota/check_version",
            headers=HEADERS,
            json=CHECK_VERSION_DATA
        )

        print(f"\n无token响应：{response.json()}")

        assert response.status_code in [401, 403], \
            f"未授权请求应返回401或403，实际返回：{response.status_code}"