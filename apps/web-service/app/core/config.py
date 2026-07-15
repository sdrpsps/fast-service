from pydantic_settings import BaseSettings


class CommonSettings(BaseSettings):
    environment: str = "development"


class WebSettings(BaseSettings):
    app_name: str = "Web Service API"

    model_config = {
        "env_file": ".env",
        "env_prefix": "WEB_",
    }


common_settings = CommonSettings()
web_settings = WebSettings()
