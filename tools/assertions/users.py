from clients.authentication.authentication_schema import LoginResponseSchema
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")

def assert_login_response(response: LoginResponseSchema):

    assert_equal(response.token.token_type, "bearer", "token_type")
    assert response.token.access_token != "", "access_token пустой"
    assert response.token.refresh_token != "", "refresh_token пустой"

def assert_get_user_response(response_data: GetUserResponseSchema, expected: CreateUserResponseSchema):
    assert_equal(response_data.user.id, expected.user.id, "id")
    assert_equal(response_data.user.email, expected.user.email, "email")
    assert_equal(response_data.user.last_name, expected.user.last_name, "last_name")
    assert_equal(response_data.user.first_name, expected.user.first_name, "first_name")
    assert_equal(response_data.user.middle_name, expected.user.middle_name, "middle_name")

def assert_user(actual: UserSchema, expected: UserSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")