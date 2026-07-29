import pytest
from pydantic import BaseModel

from clients.courses.course_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from clients.courses.courses_client import CourseClient, get_courses_client
from fixtures.files import FileFixture
from fixtures.users import function_user, UserFixture

class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema




@pytest.fixture
def courses_client(function_user: UserFixture) -> CourseClient:
    return get_courses_client(function_user.authentication_user)

@pytest.fixture
def function_course(
        courses_client: CourseClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> CourseFixture:
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)



