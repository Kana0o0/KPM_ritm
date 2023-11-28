from src.enums.global_enums import WRONG_STATUS_CODE


class Validate:
    def __init__(self, response) -> None:
        self.response = response
        self.response_json = response.json()

    def validate(self, model):
        """ Функция валидации данных используя модель pydantic """
        model.model_validate(self.response_json)
        return self


class CheckStatusCode:
    def __init__(self, response) -> None:
        self.response = response
        self.response_status = response.status_code

    def assert_status_code(self, status_code):
        """ Функция проверки статус кода """
        assert status_code == self.response_status, WRONG_STATUS_CODE
        return self
