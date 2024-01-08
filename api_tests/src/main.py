import pytest

from src.baseclasses.validate import Validate, CheckStatusCode
from src.configuration.parametrs import User


class TestPositiveAPI:
    """ Класс содержащий позитивные тесты """

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.parametrize('get_response', [{'param': User(), 'type': 'positive'}], indirect=True)
    def test_get_single_user(self, get_response):
        #  Функция создания позитивного get запроса
        Validate(response=get_response,
                 model=User.MODEL['get']).validate()
        CheckStatusCode(response=get_response,
                        status_code=User.STATUS_CODE_POSITIVE_CASE['get']).assert_status_code()

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.parametrize('get_list_response', [{'param': User(), 'type': 'positive'}], indirect=True)
    def test_get_list_user(self, get_list_response):
        #  Функция создания позитивного get_list запроса
        Validate(response=get_list_response,
                 model=User.MODEL['get_list']).validate()
        CheckStatusCode(response=get_list_response,
                        status_code=User.STATUS_CODE_POSITIVE_CASE['get']).assert_status_code()

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.parametrize('delete_response', [{'param': User(), 'type': 'positive'}], indirect=True)
    def test_delete_user(self, delete_response):
        #  Функция создания позитивного delete запроса
        CheckStatusCode(response=delete_response,
                        status_code=User.STATUS_CODE_POSITIVE_CASE['delete']).assert_status_code()

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.parametrize('post_response', [{'param': User(), 'type': 'positive'}], indirect=True)
    def test_post_user(self, post_response):
        #  Функция создания позитивного post запроса
        Validate(response=post_response,
                 model=User.MODEL['post']).validate()
        CheckStatusCode(response=post_response,
                        status_code=User.STATUS_CODE_POSITIVE_CASE['post']).assert_status_code()

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.parametrize('put_response', [{'param': User(), 'type': 'positive'}], indirect=True)
    def test_put_user(self, put_response):
        #  Функция создания позитивного put запроса
        Validate(response=put_response,
                 model=User.MODEL['put']).validate()
        CheckStatusCode(response=put_response,
                        status_code=User.STATUS_CODE_POSITIVE_CASE['put']).assert_status_code()

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.parametrize('patch_response', [{'param': User(), 'type': 'positive'}], indirect=True)
    def test_patch_user(self, patch_response):
        #  Функция создания позитивного patch запроса
        Validate(response=patch_response,
                 model=User.MODEL['patch']).validate()
        CheckStatusCode(response=patch_response,
                        status_code=User.STATUS_CODE_POSITIVE_CASE['patch']).assert_status_code()


class TestNegativeAPI:
    """ Класс содержащий негативные тесты """

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.parametrize('get_response', [{'param': User(), 'type': 'negative'}], indirect=True)
    def test_get_single_user(self, get_response):
        #  Функция создания негативного get запроса
        CheckStatusCode(response=get_response,
                        status_code=User.STATUS_CODE_NEGATIVE_CASE['get']).assert_status_code()

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.parametrize('get_list_response', [{'param': User(), 'type': 'negative'}], indirect=True)
    def test_get_list_user(self, get_list_response):
        #  Функция создания негативного get_list запроса
        CheckStatusCode(response=get_list_response,
                        status_code=User.STATUS_CODE_POSITIVE_CASE['get']).assert_status_code()

    @pytest.mark.pass_test
    @pytest.mark.positive
    @pytest.mark.parametrize('delete_response', [{'param': User(), 'type': 'negative'}], indirect=True)
    def test_delete_user(self, delete_response):
        #  Функция создания негативного delete запроса
        CheckStatusCode(response=delete_response,
                        status_code=User.STATUS_CODE_POSITIVE_CASE['delete']).assert_status_code()

    @pytest.mark.failed_test
    @pytest.mark.negative
    @pytest.mark.parametrize('post_response', [{'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_first'], 'type': 'negative'},
                                               {'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_second'], 'type': 'negative'},
                                               {'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_third'], 'type': 'negative'},
                                               {'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_fourth'], 'type': 'negative'}], indirect=True)
    def test_post_user(self, post_response):
        #  Функция создания негативного post запроса
        CheckStatusCode(response=post_response, status_code=User.STATUS_CODE_NEGATIVE_CASE['post']).assert_status_code()

    @pytest.mark.failed_test
    @pytest.mark.negative
    @pytest.mark.parametrize('put_response', [{'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_first'], 'type': 'negative'},
                                               {'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_second'], 'type': 'negative'},
                                               {'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_third'], 'type': 'negative'},
                                               {'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_fourth'], 'type': 'negative'}], indirect=True)
    def test_put_user(self, put_response):
        #  Функция создания негативного put запроса
        CheckStatusCode(response=put_response, status_code=User.STATUS_CODE_NEGATIVE_CASE['put']).assert_status_code()

    @pytest.mark.failed_test
    @pytest.mark.negative
    @pytest.mark.parametrize('patch_response', [{'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_first'], 'type': 'negative'},
                                               {'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_second'], 'type': 'negative'},
                                               {'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_third'], 'type': 'negative'},
                                               {'param': User(), 'json': User.JSON_NEGATIVE_CASE['wrong_user_fourth'], 'type': 'negative'}], indirect=True)
    def test_patch_user(self, patch_response):
        #  Функция создания негативного patch запроса
        CheckStatusCode(response=patch_response, status_code=User.STATUS_CODE_NEGATIVE_CASE['patch']).assert_status_code()
