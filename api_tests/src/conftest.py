import pytest
import requests


@pytest.fixture
def get_response(request):
    """ Фикстура для создания get запроса """
    response = requests.get(url=request.node.get_closest_marker('data').args[0])
    return response


@pytest.fixture
def delete_response(request):
    """ Фикстура для создания delete запроса """
    response = requests.delete(url=request.node.get_closest_marker('data').args[0])
    return response
