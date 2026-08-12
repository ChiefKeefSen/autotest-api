import logging

import allure

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import ExerciseSchema, CreateExerciseRequestSchema, \
    CreateExerciseResponseSchema, GetExerciseResponseSchema, GetExercisesQuerySchema, UpdateExerciseResponseSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response

logger = logging.getLogger("EXERCISES_ASSERTIONS")

@allure.step("Check create exercise response")
def assert_create_exercise_response(actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema):
    logger.info("Check create exercise response")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.course_id, expected.course_id, "course_id")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")

@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    logger.info("Check exercise")
    assert_equal(actual.id, expected.id, "exercise_id")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.order_index, expected.order_index, "order_index")

@allure.step("Check get exercise response")
def assert_get_exercise_response(
        actual: GetExerciseResponseSchema,
        expected: CreateExerciseResponseSchema
):
    logger.info("Check get exercise response")
    assert_exercise(actual.exercise, expected.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(
        actual: UpdateExerciseResponseSchema,
        expected: UpdateExerciseRequestSchema,
        function_exercise: ExerciseFixture
):
    logger.info("Check update exercise response")
    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(actual.exercise.id, function_exercise.response.exercise.id, "id")
    assert_equal(actual.exercise.course_id, function_exercise.response.exercise.course_id, "course_id")

@allure.step("Check exercise not found")
def assert_exercise_not_found(actual: InternalErrorResponseSchema):
    logger.info("Check exercise not found")
    expected = InternalErrorResponseSchema(detail="Exercise not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check get exercises response")
def assert_get_exercises_response(
        actual: GetExercisesResponseSchema,
        expected: list[ExerciseSchema]
):
    logger.info("Check get exercises response")
    assert_length(actual.exercises, expected, "exercises")
    for index, exercise in enumerate(expected):
        assert_exercise(actual.exercises[index], exercise)
