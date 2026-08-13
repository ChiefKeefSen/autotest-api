from enum import Enum


class APIRoutes(str, Enum):
    FILES = "/api/v1/files"
    USERS = "/api/v1/users"
    COURSES = "/api/v1/courses"
    EXERCISES = "/api/v1/exercises"
    AUTHENTICATION = "/api/v1/authentication"

    def __str__(self): #эта строка как раз всегда добавляет .value
        return self.value

print(f'{APIRoutes.FILES}') #т.к. это enum то строковое значение (сам путь)
                            # можно получить только через .value