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
def base_assert(_request, request_type):
    if 'post' in request_type:
        with step("Check status code for 201"):
            assert (_request.status_code == 201)
    else:
        with step("Check status code for 200"):
            assert (_request.status_code == 200)
        with step("Check response message for OK"):
            assert _request.reason == 'OK'


# request and response logging
def base_attachments(_request):
    attach(_request.url, 'request url')
    attach(str(_request.request.headers), 'request headers')
    if 'body' in _request.__dict__:
        attach(_request.request.body, 'request body')
    attach(_request.text, 'response body')


# get url based on project structure
def get_url(path):
    exec_dir = 'Executors'
    path_arr = path.rsplit('\\')
    path_arr = path_arr[path_arr.index(exec_dir) + 1:]
    add_url = ''
    for i in range(len(path_arr)):
        if path_arr[i] == path_arr[-1]:
            add_url += '/' + path_arr[-1].rsplit('.')[-2].rsplit('t_')[-1]
            return base_url + add_url
        add_url += '/' + path_arr[i]


# executor
def execute(type, url, data='', headers=content_type_header_json):
    if type == 'get':
        return requests.get(url)
    if type == 'post':
        return requests.post(url, headers=headers,  data=json.dumps(data))
