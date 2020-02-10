"""Тесты для openbrewerydb"""
import requests
import pytest
from helpers import fixed_data


@pytest.mark.parametrize('url_param, expected', fixed_data.EXPECTEDDATA)
def test_assert_json(url_param, expected):
    """Проверка данных на валидность в зависимости от переданного урла"""
    response = requests.get(url_param)
    json_dict = response.json()
    assert json_dict == expected


@pytest.mark.parametrize('url_param,expected', fixed_data.EXPECTEDID)
def test_assert_id(url_param, expected):
    """Проверка id у которых в значении присутствует query"""
    response = requests.get(url_param)
    json_dict = response.json()
    fact_list = []
    for element in json_dict:
        fact_list.append(element['id'])
    assert fact_list == expected


@pytest.mark.parametrize('url_param,expected', [('https://api.openbrewerydb.org/breweries?by_city=san_diego', 20,),
                                                ('https://api.openbrewerydb.org/breweries?by_city=moscow', 4),
                                                ('https://api.openbrewerydb.org/breweries?by_city=saint-petersburg', 0)])
def test_assert_count(url_param, expected):
    """Проверка количества пивоварен в по городам"""
    response = requests.get(url_param, expected)
    json_dict = response.json()
    count_brewery = len(json_dict)
    assert count_brewery == expected

@pytest.mark.parametrize('url_param,expected',[('https://api.openbrewerydb.org/breweries?by_city=san_diego', None),
                                               ('https://api.openbrewerydb.org/breweries?by_city=moscow', None),
                                                ('https://api.openbrewerydb.org/breweries?by_city=las-vegas', None) ])
def test_assert_list_after_clear(url_param,expected):
    """Проверка очистки словаря пивоварен"""
    response = requests.get(url_param)
    json_dict = response.json()
    assert json_dict.clear() == expected

@pytest.mark.parametrize('url_param,expected',[('https://api.openbrewerydb.org/breweries?by_city=san_diego',
                                                fixed_data.TESTKEYS),
                                               ('https://api.openbrewerydb.org/breweries?by_city=moscow',
                                                fixed_data.TESTKEYS),
                                                ('https://api.openbrewerydb.org/breweries?by_city=saint-petersburg',
                                                [])
                                               ])
def test_assert_keys(url_param,expected):
    """Проверка ключи"""
    response = requests.get(url_param)
    json_dict = response.json()
    fact_list = []
    for element in json_dict:
        fact_list = (list(element.keys()))
    assert fact_list == expected