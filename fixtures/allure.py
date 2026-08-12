import pytest

from tools.allure.environment import create_allure_environment_file


@pytest.fixture(scope="session", autouse=True) #он самостоятельно применится на каждую сессию (запуск)
def save_allure_environment_file():
    yield  #отдаем поток, после выполнения тестов выполнится след строка
    create_allure_environment_file()