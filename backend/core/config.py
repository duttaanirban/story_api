from typing import List
from pydantic import BaseSettings, field_validator

class Settings(BaseSettings):
    DATABASE_URL: str
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    ALLOWED_ORIGINS: str = ""
    OPEN_API_KEY: str

    @field_validator("ALLOWED_ORIGINS")
    def validate_allowed_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []
        
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()