from typing import Any, Sized

import allure

from tools.http.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")

@allure.step("Check that response status code is equal to {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    logger.info(f"Check that the response status code is equal to {expected}")
    assert actual == expected, (
        "Incorrect response status code. "
        f'Expected status code {expected}. '
        f'Actual status code {actual}. '
    )

@allure.step("Check that {name} is equal to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    logger.info(f"Check that the '{name}' is equal to '{expected}'")
    assert actual == expected, (
        f"Incorrect value: {name}"
        f"Expected value {expected}. "
        f"Actual value {actual}. "
    )


def assert_length(actual: Sized, expected: Sized, name: str): #Sized такой тип данный который применяется ко всему что имеет длину length
    """
    Проверяет, что длины объектов совпадают

    :param actual: Фактический объект
    :param expected: Ожидаемый объект
    :param name: Название проверяемого объекта
    :return: AssertionError: Если длины не совпадают
    """
    with allure.step(f"Check that length of {name} is equal to {len(expected)}"): #алюр шаги можно писать через контекстный менеджер если нужно в шаге указать аргументы
        logger.info(f"Check that the length of '{name}' is equal to {expected}")  #написали лог тут перед действием т.к. шаг мог не выполниться
        assert len(actual) == len(expected), (
            f"Incorrect object length: '{name}'. "
            f"Expected object length '{len(expected)}'. "
            f"Actual object length '{len(actual)}'. "
        )



