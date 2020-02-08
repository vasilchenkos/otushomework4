"""Добавим параметр через addoption и передадим его в фикстуру"""
import pytest


def pytest_addoption(parser):
    """Параметры для тестов"""
    parser.addoption('--url',
                     action='store',
                     default='https://ya.ru',
                     help='Передайте url с помощью параметра --url')


@pytest.fixture
def url_param(request):
    """Фикстура для перадачи url"""
    return request.config.getoption('--url')
