from pydantic_settings import BaseSettings

# Loads config values from enviroment variables.
class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/fastapi_db"
    
    class Config:
        env_file = ".env"

settings = Settings() # Reusable settings object that can be imported anywhere in the app