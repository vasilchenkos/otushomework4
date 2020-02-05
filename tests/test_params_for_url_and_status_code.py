"""Тест для параметра url_param"""


def test_url2(url_param, status_code_param):
    """Если в --url_param передать не ya.ru, то в status code будет 404"""
    if url_param == 'https://ya.ru':
        status_code_param = '200'
        print(url_param, status_code_param)
    else:
        status_code_param = '404'
        print(url_param, status_code_param)
        #assert False
