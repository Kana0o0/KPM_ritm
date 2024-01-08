import pytest
import requests
from requests import Response


@pytest.fixture
def get_response(request) -> Response:
    """ Функция для создания get запроса """
    if request.param['type'] == "positive":
        response = requests.get(url=request.param['param'].LINKS['get'])
    elif request.param['type'] == "negative":
        response = requests.get(url=request.param['param'].LINKS['get_nonexistent'])
    return response


@pytest.fixture
def get_list_response(request) -> Response:
    """ Функция для создания get_list запроса """
    if request.param['type'] == "positive":
        response = requests.get(url=request.param['param'].LINKS['get_list'])
    elif request.param['type'] == "negative":
        response = requests.get(url=request.param['param'].LINKS['get_nonexistent_list'])
    return response


@pytest.fixture
def delete_response(request) -> Response:
    """ Функция для создания delete запроса """
    if request.param['type'] == "positive":
        response = requests.delete(url=request.param['param'].LINKS['delete'])
    elif request.param['type'] == "negative":
        response = requests.delete(url=request.param['param'].LINKS['delete_nonexistent'])
    return response


@pytest.fixture
def post_response(request) -> Response:
    """ Функция для создания post запроса """
    if request.param['type'] == "positive":
        response = requests.post(url=request.param['param'].LINKS['post'], json=request.param['param'].JSON['all'])
    elif request.param['type'] == "negative":
        response = requests.post(url=request.param['param'].LINKS['post'], json=request.param['json'])
    return response


@pytest.fixture
def put_response(request) -> Response:
    """ Функция для создания put запроса """
    if request.param['type'] == "positive":
        response = requests.put(url=request.param['param'].LINKS['put'], json=request.param['param'].JSON['all'])
    elif request.param['type'] == "negative":
        response = requests.put(url=request.param['param'].LINKS['put'], json=request.param['json'])
    return response


@pytest.fixture
def patch_response(request) -> Response:
    """ Функция для создания patch запроса """
    if request.param['type'] == "positive":
        response = requests.patch(url=request.param['param'].LINKS['patch'], json=request.param['param'].JSON['all'])
    elif request.param['type'] == "negative":
        response = requests.patch(url=request.param['param'].LINKS['patch'], json=request.param['json'])
    return response
