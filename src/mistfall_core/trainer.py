"""Core trainer object — owns memory access and feature services."""
from typing import Optional
import logging

from src.mistfall_core.process import GameProcess
from src.mistfall_core.config import TrainerConfig
from src.services.aim_service import AimService
from src.services.esp_service import ESPService
from src.services.godmode_service import GodModeService


class Trainer:
    def __init__(self, config: TrainerConfig) -> None:
        self.cfg = config
        self.proc: Optional[GameProcess] = None
        self.log = logging.getLogger("mistfall.trainer")
        self.aim: Optional[AimService] = None
        self.esp: Optional[ESPService] = None
        self.god: Optional[GodModeService] = None

    def attach(self) -> bool:
        self.proc = GameProcess(self.cfg.process_name)
        if not self.proc.open():
            return False
        base = self.proc.module_base("MistfallHunter.exe")
        self.log.info("Attached to %s base=0x%X", self.cfg.process_name, base)

        self.aim = AimService(self.proc, self.cfg)
        self.esp = ESPService(self.proc, self.cfg)
        self.god = GodModeService(self.proc, self.cfg)
        return True

    def detach(self) -> None:
        if self.proc:
            self.proc.close()
            self.proc = None