import allure
from httpx import Request

from tools.http.curl import make_curl_from_request


def curl_event_hook(request: Request):
    """
    Event hook для автоматического прикрепления cURL к Allure отчету
    :param request: HTTP-запрос, переданный в httpx клиент
    """
    curl_command = make_curl_from_request(request)

    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)

"""
Хук (hook) — это функция-обработчик, которую фреймворк вызывает автоматически при наступлении определённого события.

В твоём проекте: httpx при каждом запросе срабатывает событие "request", и фреймворк вызывает зарегистрированный в event_hooks обработчик curl_event_hook.

Зачем нужны:

Встраивать доп. логику без изменения основного кода — не пишешь вызов в каждом запросе, а регистрируешь один раз
Единая точка для побочных действий: логирование, вложения, метрики, тайминги, ретраи
могут вызываться до выполнения функции, после и во время

Есть еще pytest хуки:
Хук             	    Когда вызывается
pytest_configure	    В начале, при конфигурации
pytest_collection	    При сборе тестов
pytest_runtest_setup	Перед каждым тестом
pytest_runtest_call	    Во время выполнения теста
pytest_runtest_teardown	После каждого теста 
pytest_sessionfinish	В конце всего прогона
pytest_report_header	Добавить строку в шапку отчёта
"""