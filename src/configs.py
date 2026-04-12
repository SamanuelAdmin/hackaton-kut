from typing import ClassVar

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    user: str
    password: str
    host: str
    port: int
    name: str

    echo: bool
    echo_pool: bool


class JWTConfig(BaseModel):
    alg: str
    secret: str


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8002


class MinioConfig(BaseModel):
    minio_bucket_name: str = "images"
    endpoint: str = "127.0.0.1"
    access_key: str = "admin"
    secret_key: str = "password"
    secure: bool = False


class Settings(BaseSettings):
    model_config: ClassVar = SettingsConfigDict(
        env_file=(".env.template", ".env", "../.env"),
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    run: RunConfig = RunConfig()
    jwt: JWTConfig
    db: DatabaseConfig
    minio: MinioConfig


settings = Settings()
