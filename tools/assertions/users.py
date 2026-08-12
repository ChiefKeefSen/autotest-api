import logging

from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema
import allure
from tools.assertions.base import assert_equal

logger = logging.getLogger("USERS_ASSERTIONS")


@allure.step("Check user")
@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info('Check create user response')

    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


@allure.step("Check get user response")
def assert_get_user_response(response_data: GetUserResponseSchema, expected: CreateUserResponseSchema):
    logger.info('Check get user response')

    assert_equal(response_data.user.id, expected.user.id, "id")
    assert_equal(response_data.user.email, expected.user.email, "email")
    assert_equal(response_data.user.last_name, expected.user.last_name, "last_name")
    assert_equal(response_data.user.first_name, expected.user.first_name, "first_name")
    assert_equal(response_data.user.middle_name, expected.user.middle_name, "middle_name")


@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    logger.info('Check user')

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")
