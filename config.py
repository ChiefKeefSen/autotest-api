from pydantic import BaseModel, HttpUrl, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


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
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="." #это делитель для вложенных моделей
        #еще __ используют, и будет что-то типо HTTP_CLIENT.URL="..."
    )

    test_data: TestDataConfig
    http_client: HTTPClientConfig

#print(Settings()) #все поля подтягиваются из .env файла

settings = Settings()





#print(
#    Settings(
#        test_data=TestDataConfig(image_png_file="C:/Users/EpticExp/Desktop/2.png"),
#        http_client=HTTPClientConfig(url="http://localhost:8000", timeout=100),
#    )
#)

# .env файл хранит файлы в формате ключ значение, хранит обычно переменные окржуения