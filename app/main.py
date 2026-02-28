from fastapi import FastAPI
from app.core.logging import configure_logging
from app.core.config import get_settings

configure_logging()

settings = get_settings()

app = FastAPI(title=settings.app_name)
