import allure

#можно шаги писать через контекстные менеджеры
#через менеджеры можно указывать много вложенных шагов например и много последовательных в одном шаге (и то и то sub steps)
def test_feature():
    with allure.step("Building API client"):
        ...  # Тут код инициализации API клиента

    with allure.step("Creating course"):
        ...  # Тут код создания курса

    with allure.step("Deleting course"):
        ...  # Тут код удаления курса



#можно через декораторы, так 1 функция это 1 шаг, sub step'ов в таком случае не будет
@allure.step("Building API client")
def build_api_client():
    ...


@allure.step("Creating course")
def create_course():
    ...


@allure.step("Deleting course")
def delete_course():
    ...


def test_feature1():
    build_api_client()
    create_course()
    delete_course()


#можно также в шагах указывать используемые аргументы функции
@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    pass


def test_feature2():
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwright")

#в отчете кода выше будут отдельные шаги (не подшаги) примерно так:
#Creating course with title "Locust" 1 parameter
#и так далее, такой шаг можно раскрыть и там будет как раз поле с параметром