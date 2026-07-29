from httpx import Response
from pydantic import BaseModel

from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, ExerciseSchema, CreateExerciseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получает список заданий для определенного курса.
        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получает информацию о задании по exercise_id.
        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создаёт задание.
        :param request: Словарь с title, courseId, maxScore,
         minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновляет данные задания.
        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore,
         minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаляет задание.
        :param exercise_id: Идентификатор задания
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> ExerciseSchema:
        """
        Метод возвращает объект в виде структуры Exercise
        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта Exercise
        """
        response = self.get_exercise_api(exercise_id)
        return ExerciseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод возвращает объект в виде структуры GetExercisesResponseDict
        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде структуры GetExercisesResponseDict
        """
        response = self.get_exercises_api(query.model_dump(by_alias=True))
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод возвращает объект в виде структуры Exercise
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде структуры Exercise
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request_body: UpdateExerciseRequestSchema) -> ExerciseSchema:
        """
        Метод возвращает объект в виде структуры Exercise
        :param exercise_id: Идентификатор задания
        :param request_body: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде структуры Exercise
        """
        response = self.update_exercise_api(exercise_id, request_body)
        return ExerciseSchema.model_validate_json(response.text)

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))