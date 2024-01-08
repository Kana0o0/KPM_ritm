from src.enums.global_enums import WRONG_STATUS_CODE


class Validate:
    def __init__(self, response, model) -> None:
        self.response = response
        self.response_json = response.json()
        self.model = model

    def validate(self):
        """ Функция валидации данных используя модель pydantic """
        self.model.model_validate(self.response_json)
        return self


class CheckStatusCode:
    def __init__(self, response, status_code) -> None:
        self.response = response
        self.response_status = response.status_code
        self.status_code = status_code

    def assert_status_code(self):
        """ Функция проверки статус кода """
        assert self.status_code == self.response_status, WRONG_STATUS_CODE
        return self
