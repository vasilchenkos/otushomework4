import requests
import pytest

# можем менять данные для ожидаемого результата
TESTDATA = [
    (['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'])]


@pytest.mark.parametrize("expected", TESTDATA)
def test_body(expected, url_param='https://dog.ceo/api/breed/hound/list'):
    """Проверяем совпадает ли ожидаемый месседж"""
    response = requests.get(url_param)
    json_dict = response.json()['message']
    assert json_dict == expected

def test_status(url_param='https://dog.ceo/api/breed/hound/afghan/images/random'):
    """Проверяем что статус в месседже success"""
    response = requests.get(url_param)
    status = response.json()['status']
    assert status == 'success'

def test_list_count_breeds(url_param='https://dog.ceo/api/breeds/list/all'):
    """Проверяем количество пород"""
    response = requests.get(url_param)
    dict_breeds = response.json()['message']
    assert len(dict_breeds) == 92

def test_get_breed(url_param='https://dog.ceo/api/breeds/list/all'):
    """Проверяем наличие породы"""
    response = requests.get(url_param)
    dict_breeds = response.json()['message']
    assert dict_breeds.get('waterdog') == ['spanish']

def test_add_breed(url_param='https://dog.ceo/api/breeds/list/all'):
    """Проверяем наличие породы после добавления"""
    response = requests.get(url_param)
    dict_breeds = response.json()['message']
    dict_breeds['terrier'] = ['russian_toy']
    assert dict_breeds.get('terrier') == ['russian_toy']
