from typing import Self

from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict

import platform
import sys

#первые 2 модели вложенные они наследуются от basemodel,
#а модель где они будут применяться всегда наследуется от BaseSettings
class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestDataConfig(BaseModel):
    image_png_file: FilePath   #конкретный путь к файлу #универсальный путь, что под мак или под винду

#эти настройки нужны чтобы их менять не трогая код,
#выносим обычно константы (не статус коды)
#нужно вообще сделать через переменные окружения
#или .env файл
#также настройки при запуске срабатывают раньше, а значит и ошибки в них первее всего выскочат
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="." #это делитель для вложенных моделей
        #еще __ используют, и будет что-то типо HTTP_CLIENT.URL="..."
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig
    allure_results_dir: DirectoryPath #буквально путь указывающий на директорию

    @classmethod
    def initialize(cls) -> Self: #возвращаемый объект есть экземпляр класса
        allure_results_dir = DirectoryPath("./allure-results")
        allure_results_dir.mkdir(exist_ok=True) #аргумент - если существует то не создам, иначе создам

        return Settings(allure_results_dir=allure_results_dir)
#print(Settings()) #все поля подтягиваются из .env файла

settings = Settings.initialize()
print(f"os_info={platform.system()}, {platform.release()}  python_version={sys.version}")
print("///////")
print("\n".join([f" {key}={value}" for key, value in settings.model_dump().items()]))




#print(
#    Settings(
#        test_data=TestDataConfig(image_png_file="C:/Users/EpticExp/Desktop/2.png"),
#        http_client=HTTPClientConfig(url="http://localhost:8000", timeout=100),
#    )
#)

# .env файл хранит файлы в формате ключ значение, хранит обычно переменные окржуения