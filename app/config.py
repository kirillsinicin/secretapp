from pydantic import MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: MongoDsn

    model_config = SettingsConfigDict(env_file=".env", env_prefix="")


settings = Settings()
