import logging
from typing import Any

import allure
from jsonschema import FormatChecker
from jsonschema.validators import Draft202012Validator, validate
logger = logging.getLogger("SCHEMA_ASSERTION")
@allure.step("Validation JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema).

    :param instance: JSON-данные, которые нужно проверить.
    :param schema: Ожидаемая JSON-schema.
    :raises jsonschema.exceptions.ValidationError: Если instance не соответствует schema.
    """
    logger.info('Validation JSON schema')
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )