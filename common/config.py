import yaml
import os

BASE_URL = "https://api-test.loonadm.com"

HEADERS = {
    "x-md-language": "zh-CN",
    "x-md-app-version": "1.0.0",
    "Content-Type": "application/json",
    "User-Agent": "Apache-HttpClient/4.5.14 (Java/18)"

}

LOGIN_DATA = {
    "email": {
        "email": "apitest9@keyirobot.com",
        "password": "apitest9"
    }
}

CHECK_VERSION_DATA = {
    "bluetooth_version": "1.0.1.ble",
    "language": "zh-Hans",
    "material_version": "1.0.6.material",
    "mcu_head_version": "1.0.3.head",
    "mcu_main_version": "1.0.4.main",
    "sn": "KY060LZPY2B5E55D",
    "version": "1.0.8",
    "version_type": {
        "type": "keyi"
    }
}

# config.py 的上一级目录就是项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 用绝对路径拼接
_data_path = os.path.join(BASE_DIR, "data", "test_data.yaml")

with open(_data_path, "r", encoding="utf-8") as f:
    TEST_DATA = yaml.safe_load(f)

LOGIN_DATA = TEST_DATA["login"]
CHECK_VERSION_DATA = TEST_DATA["check_version"]