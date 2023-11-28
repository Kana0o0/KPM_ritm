import pytest

from src.baseclasses.request import OpenPage
from src.baseclasses.validate import Validate, CheckStatusCode
from src.schema.users_schema import Users
from src.schema.single_user import Users as Single_User
from src.schema.user_created import UserCreated
from src.schema.update_user import UserUpdated
from src.builders.user import User
from src.builders.link import Link


class TestPositiveAPI:
    """ Класс содержащий позитивные тесты """

    @pytest.mark.pass_test
    @pytest.mark.positive
    def test_create_user(self):
        """ Функция запуска теста для проверки создания пользователя """
        Validate(OpenPage(Link().build(), User().build()).post_response()).validate(model=UserCreated)
        CheckStatusCode(OpenPage(Link().build(), User().build()).post_response()).assert_status_code(201)

    @pytest.mark.pass_test
    @pytest.mark.positive
    def test_update_user_by_put(self):
        """ Функция запуска теста для проверки обновления пользователя через метод put """
        Validate(OpenPage(Link().add_user('3').build(), User().build()).put_response()).validate(model=UserUpdated)
        CheckStatusCode(OpenPage(Link().add_user('3').build(), User().build()).put_response()).assert_status_code(200)

    @pytest.mark.pass_test
    @pytest.mark.positive
    def test_update_user_by_patch(self):
        """ Функция запуска теста для проверки обновления пользователя через метод patch """
        Validate(OpenPage(Link().add_user('2').build(), User().build()).patch_response()).validate(model=UserUpdated)
        CheckStatusCode(OpenPage(Link().add_user('2').build(), User().build()).patch_response()).assert_status_code(200)

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.data(Link().add_user('2').build())  # Маркер data используется для передачи параметра в фикстуру
    def test_get_single_user(self, get_response):
        """ Функция запуска теста для проверки получения одного пользователя """
        Validate(get_response).validate(model=Single_User)
        CheckStatusCode(get_response).assert_status_code(200)

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.data(Link().add_param('page', '2').build())
    def test_get_users_list(self, get_response):
        """ Функция запуска теста для проверки получения списка пользователей """
        Validate(get_response).validate(model=Users)
        CheckStatusCode(get_response).assert_status_code(200)

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.data(Link().add_user('2').build())
    def test_delete_user(self, delete_response):
        """ Функция запуска теста для проверки удаления пользователя """
        CheckStatusCode(delete_response).assert_status_code(204)


class TestNegativeAPI:
    """ Класс содержащий негативные тесты """

    @pytest.mark.failed_test
    @pytest.mark.negative
    @pytest.mark.parametrize('user_case', [
        (User().set_name(1).set_job('Python Developer').build()),
        (User().set_name('Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr.').set_job('Python Developer').build()),
        (User().set_name('Squirrel').set_job('Head of the sector of competitions for        \
                                             the supply of goods, performance of work       \
                                             and provision of services for public needs     \
                                             of the Department of Economic Development,     \
                                             Finance and Competitions of the Department     \
                                             of Consumer Market and Services of the City    \
                                             of Moscow').build()),
        (User().set_name('Squirrel').set_job(1).build(), Link().build())
    ])
    def test_create_user(self, user_case):
        """ Функция запуска теста для проверки создания нескольких отдельных пользователей с неверными данными """
        CheckStatusCode(OpenPage(Link().build(), user_case).post_response()).assert_status_code(415)

    @pytest.mark.failed_test
    @pytest.mark.negative
    @pytest.mark.parametrize('user_case, link', [
        (User().set_name(1).set_job('Python Developer').build(), Link().build()),
        (User().set_name('Ellen Georgian Ser-Lecken').set_job('Python Developer').build(), Link().build()),
        (User().set_name('Squirrel').set_job('Head of the sector of competitions for            \
                                                 the supply of goods, performance of work       \
                                                 and provision of services for public needs     \
                                                 of the Department of Economic Development,     \
                                                 Finance and Competitions of the Department     \
                                                 of Consumer Market and Services of the City    \
                                                 of Moscow').build(), Link().build()),
        (User().set_name('Squirrel').set_job('Python Developer').build(), Link().add_user('13').build()),
        (User().set_name('Squirrel').set_job(1).build(), Link().build())
    ])
    def test_update_user_by_put(self, user_case, link):
        """ Функция запуска теста для проверки обновления нескольких отдельных
            пользователей с неверными данными с помощью метода put"""
        CheckStatusCode(OpenPage(link, user_case).put_response()).assert_status_code(415)

    @pytest.mark.failed_test
    @pytest.mark.negative
    @pytest.mark.parametrize('user_case, link', [
        (User().set_name(1).set_job('Python Developer').build(), Link().build()),
        (User().set_name('Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr.').set_job('Python Developer').build(), Link().build()),
        (User().set_name('Squirrel').set_job('Head of the sector of competitions for            \
                                                 the supply of goods, performance of work       \
                                                 and provision of services for public needs     \
                                                 of the Department of Economic Development,     \
                                                 Finance and Competitions of the Department     \
                                                 of Consumer Market and Services of the City    \
                                                 of Moscow').build(), Link().build()),
        (User().set_name('Squirrel').set_job('Python Developer').build(), Link().add_user('13').build()),
        (User().set_name('Squirrel').set_job(1).build(), Link().build())
    ])
    def test_update_user_by_patch(self, user_case, link):
        """ Функция запуска теста для проверки обновления нескольких отдельных
              пользователей с неверными данными с помощью метода patch"""
        CheckStatusCode(OpenPage(link, user_case).patch_response()).assert_status_code(415)

    @pytest.mark.pass_test
    @pytest.mark.negative
    @pytest.mark.data(Link().add_user('13').build())
    def test_get_unknown_single_user(self, get_response):
        """ Функция запуска теста для проверки получения несуществующего пользователя """
        CheckStatusCode(get_response).assert_status_code(404)

    @pytest.mark.failed_test
    @pytest.mark.negative
    @pytest.mark.data(Link().add_param('page', '3').build())
    def test_get_users_list(self, get_response):
        """ Функция запуска теста для проверки получения списка пользователей на несуществующей странице """
        CheckStatusCode(get_response).assert_status_code(404)

    @pytest.mark.failed_test
    @pytest.mark.negative
    @pytest.mark.data(Link().add_user('13').build())
    def test_delete_user(self, delete_response):
        """ Функция запуска теста для проверки удаления несуществующего пользователя """
        CheckStatusCode(delete_response).assert_status_code(404)
