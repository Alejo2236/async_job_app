from fastapi import FastAPI
from app.core.logging import configure_logging


configure_logging()

app = FastAPI()
