from enum import Enum


class AllureStory(str, Enum): #story это уже что-то конкретное, какие-то операции, функции
    LOGIN = "login"

    GET_ENTITY = "Get entity"
    GET_ENTITIES = "Get entities"
    CREATE_ENTITY = "Create entity"
    UPDATE_ENTITY = "Update entity"
    DELETE_ENTITY = "Delete entity"
    VALIDATE_ENTITY = "Validate entity"