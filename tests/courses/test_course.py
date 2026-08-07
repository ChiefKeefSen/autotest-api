from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.courses.courses_client import CourseClient
from clients.courses.course_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
class TestCourses:
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("Update course")
    @allure.severity(Severity.CRITICAL)
    def test_update_course(self, courses_client: CourseClient, function_course: CourseFixture):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(function_course.response.course.id, request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("Get courses")
    @allure.story(AllureStory.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_get_courses(
            self,
            courses_client: CourseClient,
            function_user: UserFixture,
            function_course: CourseFixture
    ):

        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create course")
    @allure.severity(Severity.BLOCKER)
    def test_create_course(self, courses_client: CourseClient, function_user: UserFixture, function_file: FileFixture):
        request = CreateCourseRequestSchema(
            createdByUserId=function_user.response.user.id,
            previewFileId=function_file.response.file.id
        )
        response = courses_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(request, response_data)



    #чтоб запустить тесты с итоговым отчетом в allure (например по флагу "regression")
    #надо написать: pytest -m "regression" --alluredir=./allure-results
    #чтоб отобразить отчет: allure serve ./allure-results
    #таким образом локально поднимается сервер на котором уже можно посмотреть отчет
    #если мы хотим статический то из папки с отчетами его генерируем
    #allure generate ./allure-results --output=./allure-report
    #по сути есть только
    # --alluredir=    при запуске
    # allure serve    для локального сервера
    # allure generate    для отчета


    #Epic     = крупная бизнес-область всей системы
    #  └─ Feature = модуль/сущность API (модуль с тестами)
    #       └─ Story = конкретный сценарий (CRUD-операция)


    #BLOCKER - уровень важности функционала,
    # если такой функционал не работает приложение становится неработоспособным буквально

    #CRITICAL - если функционал такого уровня падает то приложением пользоваться можно,
    # но с точки зрения бизнес логики он бесполезен, в банке невозможно оперировать деньгами например

    #NORMAL - если функционал такого уровня падает, то пользоваться приложением также можно, но не совсем удобно
    # магазин работает, но по карте не принимают, есть обходные пути но это неудобно

    #MINOR - если что-то не работает, но приложение полностью функционально
    #не работает какая-то редкоиспользуемая функция, не влияющая на основную бизнес логику

    #TRIVIAL - опечатка в тексте, смещение на пиксель, цвет на тон больше меньше