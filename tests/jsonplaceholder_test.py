import pytest
import requests

from helpers import fixed_data


@pytest.mark.parametrize('url_param, expected', fixed_data.DATAJSONPLACEHOLDER)
def test_assert_get_json(url_param, expected):
    """Проверяем месседж которые получили"""
    response = requests.get(url_param)
    json_dict = response.json()
    assert json_dict == expected


@pytest.mark.parametrize('input_body, expected_body',
                         [
                             ('ololo', 'ololo'),
                             ('', ''),
                             ('hello', 'hello')
                         ])
def test_assert_post_body(input_body, expected_body, url_param='https://jsonplaceholder.typicode.com/posts/'):
    """Проверяем что ушло в title"""
    response = requests.post(url_param, data={
        'title': input_body,
    }).json()
    print(response)
    assert response['title'] == expected_body


def test_assert_id(url_param='https://jsonplaceholder.typicode.com/posts/1/comments', expected=500):
    """Проверясм количество комментов"""
    response = requests.get(url_param)
    json_dict = response.json()
    fact_list = []
    for element in json_dict:
        fact_list.append(element['id'])
    assert len(fact_list) == expected


def test_assert_fields(url_param='https://jsonplaceholder.typicode.com/comments?postId=1', expected=None):
    """Проверяем что после очищения список пустой"""
    response = requests.get(url_param)
    json_dict = response.json()
    assert json_dict.clear() == expected


def test_assert_email_count(url_param='https://jsonplaceholder.typicode.com/posts/1/comments', expected=0):
    """Проверяем что почты в списке нет"""
    response = requests.get(url_param)
    json_dict = response.json()
    assert json_dict.count('ololo@mail.ru') == expected
