from httpx import Request, RequestNotRead, post, Client

"""
curl -X 'PATCH' \
  'http://localhost:8000/api/v1/users/5ece37fc-fb0a-4dfb-a6aa-c7aa1d93bfb6' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOiIyMDI2LTA4LTA3VDE1OjA5OjMyLjYwNjYyMyIsInVzZXJfaWQiOiJhYTNkNTU4Mi02NjRlLTQ5YzgtOWFjYy0wZWZiM2YwMTZjYmQifQ.VsFoIvgjbCzOBQwmtsoZ3loZhWL3nW6BG2hs4fe-BQI' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "userasdfd@example.com",
  "lastName": "string3123",
  "firstName": "strinfg",
  "middleName": "strinfg"
}'
"""
"""
curl -X 'POST' \
  'http://localhost:8000/api/v1/users' \
  -H 'host: localhost:8000' \
  -H 'accept: */*' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'connection: keep-alive' \
  -H 'user-agent: python-httpx/0.28.1' \
  -H 'content-length: 105' \
  -H 'content-type: application/json' \
  -d '{"id":"string","email":"user@example.com","lastName":"string","firstName":"string","middleName":"string"}'

"""
def make_curl_from_request(request: Request):
    """
    Генерирует команду cURL из HTTP-запроса httpx
    :param request: HTTP-запрос из которого будет сформирована команда cURL
    :return: Строка с командой cURL, содержащая метод запроса, URL, заголовки, тело (если есть)
    """
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")
    try:
        if body := request.content: #:= означает присвоить в переменную и сразу использовать
            result.append(f"-d '{body.decode('utf-8')}'")
    except RequestNotRead:
        pass

    return " \\\n  ".join(result)

#body = {
#    "id": "string",
#    "email": "user@example.com",
#    "lastName": "string",
#    "firstName": "string",
#    "middleName": "string"
#  }
#response = post("http://localhost:8000/api/v1/users", json=body)
#print(make_curl_from_request(response.request))


#механика хуков событий
#def print_request(request: Request): #это короче функция обработчик
#    print(f"Выполняем запрос {request.method}") #сработает когда выполнится хук
#
#client = Client(event_hooks={"request": [print_request]})  #event_hooks - когда встретится событие request (а оно зарезервированно, поэтому буквально каждый запрос это событие request)
#client.get("http://localhost:8000/api/v1/users")           #то тогда выполнится список из функций обработчиков (поэтому у нас список из 1 элемента)
#client.post("http://localhost:8000/api/v1/users")          #и получается что на каждый request у нас будет выполняться фукнция обработчик
#client.patch("http://localhost:8000/api/v1/users")
#client.delete("http://localhost:8000/api/v1/users")