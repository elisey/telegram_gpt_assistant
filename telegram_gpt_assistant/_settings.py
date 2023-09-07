import pydantic
import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    telegram_bot_token: str

    openai_api_key: str
    system_prompt: str
    history_size: int
    history_ttl: int

    start_message: str

    @property
    def allowed_users(self) -> list[str]:
        users = self.allowed_users_raw.split(",")
        if users == [""]:
            return []
        return [user.strip() for user in users]

    # don't use this, use allowed_users instead
    allowed_users_raw: str = pydantic.Field(alias="allowed_users")

    model_config = pydantic_settings.SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
