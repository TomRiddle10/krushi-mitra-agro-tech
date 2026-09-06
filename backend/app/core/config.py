import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv(
        "APP_NAME",
        "Krushi Mitra Agro Tech"
    )

    ENVIRONMENT: str = os.getenv(
        "ENVIRONMENT",
        "development"
    )

    SUPABASE_URL: str = os.getenv(
        "SUPABASE_URL",
        ""
    )

    SUPABASE_KEY: str = os.getenv(
        "SUPABASE_KEY",
        ""
    )


settings = Settings()