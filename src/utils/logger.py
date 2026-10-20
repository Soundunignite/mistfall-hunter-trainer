"""Logging setup for the trainer."""
import logging
from pathlib import Path


def setup_logging(log_dir: str = "logs") -> None:
    Path(log_dir).mkdir(exist_ok=True)
    fmt = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        handlers=[
            logging.FileHandler(f"{log_dir}/trainer.log", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )