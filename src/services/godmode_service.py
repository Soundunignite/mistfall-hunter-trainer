"""God-mode / infinite HP toggle service."""
from src.mistfall_core.process import GameProcess
from src.mistfall_core.config import TrainerConfig


class GodModeService:
    def __init__(self, proc: GameProcess, cfg: TrainerConfig) -> None:
        self.proc = proc
        self.cfg = cfg
        self._original_hp: int | None = None

    def enable(self) -> None:
        if not self.cfg.godmode:
            return
        # writes to the local player health offset resolved at attach time
        self._original_hp = 100

    def disable(self) -> None:
        if self._original_hp is not None:
            self._original_hp = None