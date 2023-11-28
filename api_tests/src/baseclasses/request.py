import requests


class OpenPage:

    def __init__(self, url, json=None) -> None:
        self.url = url
        self.response_json = json

    def post_response(self):
        """ Функция для создания post запроса """
        response = requests.post(url=self.url, json=self.response_json)
        return response

    def put_response(self):
        """ Функция для создания put запроса """
        response = requests.put(url=self.url, json=self.response_json)
        return response

    def patch_response(self):
        """ Функция для создания patch запроса """
        response = requests.patch(url=self.url, json=self.response_json)
        return response
