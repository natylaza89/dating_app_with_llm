import os
from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


class Settings(BaseSettings):
    def __init__(self, **kwargs):
        load_dotenv()
        super().__init__(**kwargs)

    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        arbitrary_types_allowed=True,
        extra="ignore",
        env_file=".env"
    )

    app_env: str = os.environ.get("APP_ENV", "dev")
    project_name: str = "dating-app"
    api_v1_str: str = "/api/v1"
    allowed_hosts: list[str] = ["localhost", "127.0.0.1"]
    fastapi_info: ClassVar = (
        {"openapi_url": f"{api_v1_str}/openapi.json", "docs_url": "/docs"}
        if app_env == "dev"
        else {}
    )
    app_string: str = "app.main:app"
    mock_llm: bool = os.environ.get("MOCK_LLM") in {"True", "true"}
    cohere_api_key: str = os.environ.get("COHERE_API_KEY", "")


settings = Settings()
