from httpx import Client

from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook

from config import settings

def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        event_hooks=
        {
            "request": [curl_event_hook, log_request_event_hook], #до выполнения запроса логируется курл запроса и прикрепляется к нему (1функция) и в терминал логируется запрос
            "response": [log_response_event_hook] #тут логируется ответ запроса
        }
        #до выполнения это request
        #во время это например, замерка времени от начала и до конца ->
        #после это response

        #def request_hook(request: Request):
        #    global start_time
        #    start_time = time.time()  # старт таймера ДО

        #def response_hook(response: Response):
        #    duration = time.time() - start_time  # финиш ПОСЛЕ
        #    logger.info(f"Запрос занял {duration:.2f}s")
        #    return response

        #есть еще спец функция которая выполняется до каждого теста
        #pytest_runtest_setup(test) (имя зарезервированно)
        #и есть которая после теста
        #pytest_runtest_teardown(test)
        
    )