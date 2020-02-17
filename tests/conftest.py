"""Добавим параметр через addoption и передадим его в фикстуру"""
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
                     help='Передайте status_code с помощью параметра --status_code')


@pytest.fixture
def url_param(request):
    """Фикстура для перадачи url"""
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request):
    """Фикстура для перадачи url"""
    return request.config.getoption('--status_code')
