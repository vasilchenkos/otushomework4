"""Добавим параметры через addoption и передадим их в фикстуры"""
import pytest

def pytest_addoption(parser):
    """Параметры для тестов"""
    parser.addoption('--url',
                     action='store',
                     default='https://ya.ru',
                     help='Передайте url с помощью параметра --url')

    parser.addoption('--status_code',
                     action='store',
                     default='200',
                     help='Передайте --status_code с помощью параметра --status_code')


@pytest.fixture
def url_param(request):
    """Фикстура для перадачи url """
    return request.config.getoption('--url')

@pytest.fixture
def status_code_param(request):
    """Фикстура для перадачи status code """
    return request.config.getoption('--status_code')
