from fastapi import FastAPI
from app.core.logging import configure_logging
from app.core.config import get_settings

settings = get_settings()

configure_logging(
    log_level=settings.log_level,
    log_to_file=settings.log_to_file,
    log_file_path=settings.log_file_path,
)

app = FastAPI(title=settings.app_name)
