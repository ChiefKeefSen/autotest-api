from enum import Enum


class AllureEpic(str, Enum): #эпики это скорее большие системы, сервисы
    LMS = "LMS service"
    STUDENT = "Student service"
    ADMINISTRATION = "Administration service"