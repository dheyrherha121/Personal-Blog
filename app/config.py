from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    database_name:str
    database_username: str
    database_hostname: str
    database_password: str
    database_port: int
    secret_key: str
    algorithm: str
    expires_minutes: int

    model_config = SettingsConfigDict(env_file= '.env')

setting = Setting()