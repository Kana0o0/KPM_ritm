from faker import Faker


fake = Faker('fr_FR')  # Выбранный язык французский, для изменения на русский использовать ru_RU


class User:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_name(self, name=None):
        """ Функция для создания имени пользователя """
        if name is None:
            self.result['name'] = fake.first_name()  # В случае отсутствия ручного ввода генерирует случайное имя
        else:
            self.result['name'] = name
        return self

    def set_job(self, job=None):
        """ Функция для создания работы пользователя """
        if job is None:
            self.result['job'] = fake.job()  # В случае отсутствия ручного ввода генерирует случайную работу
        else:
            self.result['job'] = job
        return self

    def reset(self):
        self.set_name()
        self.set_job()
        return self

    def build(self):
        """ Функция для генерации пользователя """
        return self.result
