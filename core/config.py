import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_user: str = "autoinsight_user"
    db_password: str = "autoinsight_password"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "autoinsight"
    
    drop_duplicates: bool = True
    handle_missing: bool = True
    
    # Allows reading from .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8', extra='ignore')

    @property
    def database_url(self):
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()
