from pydantic_settings import BaseSettings #BaseSettings class that reads .env file


class Settings(BaseSettings):
    # App
    APP_NAME: str = "AI POS System"
    DEBUG: bool = True

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database
    DATABASE_URL: str

    # Redis
    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"


settings = Settings()