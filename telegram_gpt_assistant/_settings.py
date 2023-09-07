import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    telegram_bot_token: str

    openai_api_key: str
    system_prompt: str
    history_size: int
    history_ttl: int

    start_message: str

    model_config = pydantic_settings.SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
