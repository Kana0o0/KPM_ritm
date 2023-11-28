from src.configuration.configuration import USERS


class Link:
    """ Класс для генерации ссылок ресурса """

    def __init__(self):
        self.result = USERS
        self.reset()

    def add_user(self, id_user: str = None):
        """ Функция создания параметра пользователя """
        if id_user:
            self.result = self.result + "/" + id_user
        else:
            return self
        return self

    def add_param(self, param: str = None, value: str = None):
        """ Функция создания параметра страниц """
        if param and value:
            self.result = self.result + f'?{param}={value}'
        else:
            return self
        return self

    def reset(self):
        self.add_user()
        self.add_param()
        return self

    def build(self) -> str:
        """ Функция создает ссылку """
        return self.result
