import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from dotenv import load_dotenv


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        arbitrary_types_allowed=True,
        extra="ignore",
        env_file=".env",
        case_sensitive=False,
    )

    app_env: str = Field(default="dev")
    project_name: str = "dating-app"
    api_v1_str: str = "/api/v1"
    app_string: str = "app.main:app"
    mock_llm: bool = Field(default=False)
    cohere_api_key: str = Field(default="")

    @property
    def fastapi_info(self) -> dict:
        return (
            {"openapi_url": f"{self.api_v1_str}/openapi.json", "docs_url": "/docs"}
            if self.app_env == "dev"
            else {}
        )

    def model_post_init(self, __context) -> None:
        load_dotenv()
        self.mock_llm = os.environ.get("MOCK_LLM", "").lower() in {"True", "true"}
        self.cohere_api_key = os.environ.get("COHERE_API_KEY", "")
        

settings = Settings()
