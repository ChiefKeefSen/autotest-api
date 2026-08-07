import allure

from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_equal


@allure.step("Check login response")
def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет корректность ответа при успешной авторизации
    :param response: Объект ответа с токенами авторизации
    :raises: AssertionError: Если какое-либо из условий не выполняется
    """
    assert_equal(response.token.token_type, "bearer", "token_type")
    assert response.token.access_token != "", "access_token пустой"
    assert response.token.refresh_token != "", "refresh_token пустой"
