"""Dev launcher — attaches and starts console for quick iteration."""
from src.utils.logger import setup_logging
from src.mistfall_core.config import load_config
from src.mistfall_core.trainer import Trainer
from src.handlers.console_handler import run_console
from pathlib import Path


def main() -> None:
    setup_logging()
    cfg = load_config(Path("config/default.yaml"))
    trainer = Trainer(cfg)
    if not trainer.attach():
        print("attach failed — is Mistfall Hunter running?")
        return
    try:
        run_console(trainer)
    finally:
        trainer.detach()


if __name__ == "__main__":
    main()