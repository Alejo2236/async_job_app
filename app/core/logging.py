import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


FIVE_MB_IN_BYTES: int = 5 * 1024 * 1024


def configure_logging(
    log_level: str = "INFO",
    log_to_file: bool = True,
    log_file_path: str = "logs/app.log",
) -> None:
    """
    Configure application logging.

    Args:
        log_level: Logging level (e.g., INFO, DEBUG).
        log_to_file: Whether to enable file logging.
        log_file_path: Path to the log file.
    """

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    handlers = []

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    handlers.append(console_handler)

    if log_to_file:
        log_path = Path(log_file_path)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_path,
            maxBytes=FIVE_MB_IN_BYTES,
            backupCount=3,
        )
        file_handler.setFormatter(formatter)
        handlers.append(file_handler)

    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        handlers=handlers,
    )
