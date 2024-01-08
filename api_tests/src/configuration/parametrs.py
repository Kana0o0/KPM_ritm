from src.builders.link import Link
from src.builders.user import User
from src.schema.single_user import SingleUser
from src.schema.update_user import UserUpdated
from src.schema.user_created import UserCreated
from src.schema.users_schema import UsersList


class User:
    #  Позитивные статус коды для User
    STATUS_CODE_POSITIVE_CASE = {'get': 200,
                                 'post': 201,
                                 'put': 200,
                                 'patch': 200,
                                 'delete': 204}

    #  Негативные статус коды для User
    STATUS_CODE_NEGATIVE_CASE = {'get': 404,
                                 'post': 415,
                                 'put': 415,
                                 'patch': 415,
                                 'delete': 404}

    #  Позитивные JSON модели для User
    JSON = {'all': User().build()}

    #  Негативные JSON модели для User
    JSON_NEGATIVE_CASE = {'wrong_user_first': User().set_name(1).set_job('Python Developer').build(),
                          'wrong_user_second': User().set_name('Hubert Blaine                      \
                                                         Wolfeschlegelsteinhausenbergerdorff \
                                                         Sr.').set_job('Python Developer').build(),
                          'wrong_user_third': User().set_name('Squirrel').set_job('Head of the sector of competitions for \
                                             the supply of goods, performance of work       \
                                             and provision of services for public needs     \
                                             of the Department of Economic Development,     \
                                             Finance and Competitions of the Department     \
                                             of Consumer Market and Services of the City    \
                                             of Moscow').build(),
                          'wrong_user_fourth': User().set_name('Squirrel').set_job(1).build()}

    # Ссылки ресурса для user
    LINKS = {'get': Link().add_user('3').build(),
             'get_nonexistent': Link().add_user('84').build(),
             'get_list': Link().add_param('page', '2').build(),
             'get_nonexistent_list': Link().add_param('page', '39').build(),
             'post': Link().build(),
             'put': Link().add_user('3').build(),
             'patch': Link().add_user('3').build(),
             'delete': Link().add_user('2').build(),
             'delete_nonexistent': Link().add_user('93').build()}

    # Модели для user
    MODEL = {'get': SingleUser,
             'get_list': UsersList,
             'post': UserCreated,
             'put': UserUpdated,
             'patch': UserUpdated}
