import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

FIVE_MB_IN_BYTES: int = 5 * 1024 * 1024


def configure_logging():
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=FIVE_MB_IN_BYTES,
        backupCount=3,
    )
    file_handler.setFormatter(formatter)

    logging.basicConfig(
        level=logging.INFO,
        handlers=[console_handler, file_handler],
    )
