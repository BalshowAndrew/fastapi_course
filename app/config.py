from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    #MODE: Literal["DEV", "TEST", "PROD"]
    #LOG_LEVEL: str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: int
    DB_NAME: str
    
    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()


#print(settings.DATABASE_URL)
