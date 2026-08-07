import allure
import pytest
from allure_commons.types import Severity

from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus

from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response


@pytest.mark.regression
@pytest.mark.users
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION) #в тэгах всегда UPPER_SNAKE_CASE
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
class TestUsers:
    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create user")
    @allure.severity(Severity.BLOCKER)
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):
        #allure.title(f"Create user: {email}") #этим злоупотреблять не стоит, тем более для параметров
        # делаем клиент, тело запроса, с помощью клиента кидаем запрос на создания пользователя и получаем ответ
        request = CreateUserRequestSchema()
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)  # мы валидируем ответ тут со схемой, но если попадется "1", то это будет тип int поэтому дальше есть вторая валидация

        # assert response.status_code == HTTPStatus.OK, "Некорректный статус код ответа" #проверяем статус код и дальше проверяем все ли поля те же самые что ушли
        assert_status_code(response.status_code, HTTPStatus.OK)  # эквивалент вышестоящей строчки кода

        # assert response_data.user.email == request.email, "Некорректный email пользователя"
        # assert response_data.user.first_name == request.first_name, "Некорректный first_name пользователя"
        # assert response_data.user.last_name == request.last_name, "Некорректный last_name пользователя"
        # assert response_data.user.middle_name == request.middle_name, "Некорректный middle_name пользователя"

        assert_create_user_response(request, response_data)  # аналог вышестоящих строк, проверяем что значения, которые отправляли вернулись те же самые

        validate_json_schema(response.json(), response_data.model_json_schema())  # response_data.model_json_schema() генерирует схему на основе CreateUserResponseSchema и проверяет по ней ответ
        # можно сказать что в строке выше мы проверяем уже структуру и типы значений, а сами значения проверяем на 25-ой

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("Get user me")
    @allure.story(AllureStory.GET_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_get_user_me(self, function_user: UserFixture, private_users_client: PrivateUsersClient):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)

        validate_json_schema(response.json(), response_data.model_json_schema())


