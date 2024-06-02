from pydantic_settings import BaseSettings


class base_settings(BaseSettings):
    BASE_USER: str = "ecomusic"
    BASE_PASSWORD: str = "1337228fffR"
    BASE_HOST: str = "localhost"
    BASE_TABLE: str = "ecomusic"


base_config = base_settings()
