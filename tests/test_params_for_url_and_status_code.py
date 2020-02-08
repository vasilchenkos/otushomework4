"""Тест для параметра url_param"""

import requests

def test_url_and_status_code(url_param):
    """Тест для проверки status_code"""
    response = requests.get(url_param)
    assert response.status_code == 200
    print('status_code is OK \n' + str(response))
