from telegram_gpt_assistant._settings import Settings


def test_allowed_users() -> None:
    settings = Settings(
        telegram_bot_token="token",
        openai_api_key="api key",
        system_prompt="Your system prompt",
        history_size=10,
        history_ttl=3600,
        start_message="Hello, this is the start message.",
        allowed_users="user1,user2, user3",
    )

    assert settings.allowed_users == ["user1", "user2", "user3"]


def test_allowed_users_one() -> None:
    settings = Settings(
        telegram_bot_token="token",
        openai_api_key="api key",
        system_prompt="Your system prompt",
        history_size=10,
        history_ttl=3600,
        start_message="Hello, this is the start message.",
        allowed_users="123456",
    )

    assert settings.allowed_users == ["123456"]


def test_allowed_users_empty() -> None:
    settings = Settings(
        telegram_bot_token="token",
        openai_api_key="api key",
        system_prompt="Your system prompt",
        history_size=10,
        history_ttl=3600,
        start_message="Hello, this is the start message.",
        allowed_users="",
    )

    assert settings.allowed_users == []
