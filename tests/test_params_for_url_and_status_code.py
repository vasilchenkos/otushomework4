"""Тест для параметра url_param"""

import requests


def test_url_and_status_code(url_param, status_code):
    """Тест для проверки status_code"""
    response = requests.get(url_param)
    status_code = response.status_code
    assert status_code == 200
    print('status_code is OK ' + str(status_code))
