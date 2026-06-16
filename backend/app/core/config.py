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
    
    # AI
    GROQ_API_KEY: str  

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


settings = Settings()