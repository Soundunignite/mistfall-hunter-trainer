"""ESP / wallhack service — renders entity boxes via overlay."""
from typing import List

from src.mistfall_core.process import GameProcess
from src.mistfall_core.config import TrainerConfig


class ESPEntity:
    __slots__ = ("name", "x", "y", "z", "health", "distance")

    def __init__(self, name: str, x: float, y: float, z: float,
                 health: int, distance: float) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.health = health
        self.distance = distance


class ESPService:
    def __init__(self, proc: GameProcess, cfg: TrainerConfig) -> None:
        self.proc = proc
        self.cfg = cfg

    def collect(self) -> List[ESPEntity]:
        if not self.cfg.esp.enabled:
            return []
        entities: List[ESPEntity] = []
        # entity list resolution happens in offset_dumper output
        return entities

    def filter(self, entities: List[ESPEntity]) -> List[ESPEntity]:
        return [e for e in entities if e.distance <= self.cfg.esp.max_range]