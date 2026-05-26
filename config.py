from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Configuración de la aplicación."""
    
    # Aplicación
    APP_NAME: str = "Gestion Profesoral API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Base de datos - variables planas del .env
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "gestion_profesoral"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Obtiene la configuración cacheada."""
    return Settings()