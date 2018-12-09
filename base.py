from allure import step, attach
from config import *
import requests
import json


# collecting base headers
def base_headers():
    return {}
    # return {'Authorization': get_token(login)}


# get resulting dictionary
def dict_add(*args):
    sum_dict = dict()
    for arg in args:
        sum_dict.update(arg)
    return sum_dict


# base checks
def base_assert(_request):
    with step("Проверка Status Code на 201"):
        assert _request.status_code == 201
    # with step("Проверка Response Message на OK"):
    #     assert _request.reason == 'OK'
    with step("Проверка Response Body на отсутсвие Errors"):
        if 'Errors' not in _request.text:
            assert True
        else:
            assert len(json.loads(_request.text)['Errors']) == 0


# request and response logging
def base_attachments(_request):
    attach(_request.url, 'request url')
    attach(str(_request.request.headers), 'request headers')
    attach(_request.request.body, 'request body')
    attach(_request.text, 'response body')


# get url based on project structure
def get_url(path):
    path_arr = path.rsplit('\\')
    return base_url + '/' + path_arr[-2] + '/' + path_arr[-1].rsplit('.')[-2]


# executor
def execute(type, url, data='', headers=content_type_header_json):
    if type == 'get':
        return requests.get(url)
    if type == 'post':
        # header = dict_add(base_headers, headers)
        return requests.post(url, data=json.dumps(data))
