"""Entry point for the Mistfall Hunter Trainer."""
import sys
import logging
from pathlib import Path

from src.mistfall_core.trainer import Trainer
from src.mistfall_core.config import load_config
from src.overlay.hud import OverlayHUD
from src.utils.logger import setup_logging


def main() -> int:
    setup_logging()
    log = logging.getLogger("mistfall.bootstrap")
    log.info("Mistfall Hunter Trainer starting...")

    cfg = load_config(Path("config/default.yaml"))
    trainer = Trainer(cfg)

    if not trainer.attach():
        log.error("Failed to attach to Mistfall Hunter process")
        return 1

    hud = OverlayHUD(trainer)
    try:
        hud.run()
    except KeyboardInterrupt:
        log.info("Shutdown requested")
    finally:
        trainer.detach()
    return 0


if __name__ == "__main__":
    sys.exit(main())