from enum import Enum


class AllureFeature(str, Enum): #под scope feature попадают модули с тестами
    USERS = "users"
    FILES = "files"
    COURSES = "courses"
    EXERCISES = "exercises"
    AUTHENTICATION = "authentication"
