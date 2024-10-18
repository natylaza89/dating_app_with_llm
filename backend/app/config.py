import os
from typing import ClassVar

from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    environment: str = os.environ.get("ENV", "dev")
    project_name: str = "dating-app"
    api_v1_str: str = "/api/v1"
    allowed_hosts: list[str] = ["localhost", "127.0.0.1"]
    fastapi_info: ClassVar = (
        {"openapi_url": f"{api_v1_str}/openapi.json", "docs_url": "/docs"}
        if environment == "dev"
        else {}
    )
    app_string: str = "app.main:app"
    mock_llm: bool = bool(os.environ.get("MOCK_LLM", "0"))

    model_config = ConfigDict(
        env_nested_delimiter="__",
        arbitrary_types_allowed=True,
        extra="ignore",
        env_file=("../.env" if os.getenv("ENV", "dev") == "dev" and os.path.exists("../.env") else ".env")
    )

settings = Settings()
