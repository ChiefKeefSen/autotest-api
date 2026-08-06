from http import HTTPStatus

import allure
import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUsersClient

from fixtures.users import UserFixture
from tools.allure.tags import AllureTag

from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_login_response



@pytest.mark.authentication
@pytest.mark.regression
@allure.tag(AllureTag.AUTHENTICATION)
class TestAuthentication:
    @allure.title("Login with correct email and password")
    def test_login(self, function_user: UserFixture, public_users_client: PublicUsersClient,
                   authentication_client: AuthenticationClient):
        login_request = LoginRequestSchema(
            email=function_user.email,
            password=function_user.password
        )
        response = authentication_client.login_api(login_request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)