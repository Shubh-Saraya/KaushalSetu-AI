import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str = "sqlite:///./kaushalsetu.db"
    gemini_api_key: str = ""
    secret_key: str = "demo-secret-key-for-development-only"
    frontend_url: str = "http://localhost:5173"

    class Config:
        env_file = ".env"


settings = Settings()
