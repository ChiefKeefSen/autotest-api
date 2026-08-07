from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUsersClient

from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag

from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response


@pytest.mark.authentication
@pytest.mark.regression
@allure.tag(AllureTag.AUTHENTICATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @allure.tag(AllureStory.LOGIN)
    @allure.title("Login with correct email and password")
    @allure.severity(Severity.BLOCKER)
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