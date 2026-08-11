from pydantic import BaseModel, Field
from tools.http.fakers import fake

class TokenSchema(BaseModel):
    """
    Содержит информацию о структуре токена
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """
    Содержит информацию о необходимых полях для логина
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)

class RefreshRequestSchema(BaseModel):
    """
    Содержит информацию о необходимых полях для refresh токена
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)


class LoginResponseSchema(BaseModel):
    """Описание структуры ответа на аутентификацию"""
    token: TokenSchema


