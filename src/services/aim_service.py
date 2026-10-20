"""Aimbot service — computes target angles and writes to camera."""
import math
from dataclasses import dataclass

from src.mistfall_core.process import GameProcess
from src.mistfall_core.config import TrainerConfig
from src.mistfall_core.signatures import by_name


@dataclass
class Vec3:
    x: float
    y: float
    z: float


class AimService:
    def __init__(self, proc: GameProcess, cfg: TrainerConfig) -> None:
        self.proc = proc
        self.cfg = cfg
        self._sig = by_name("local_player")

    def _local_pos(self) -> Vec3:
        # placeholder: real offset resolution lives in offset_dumper
        return Vec3(0.0, 0.0, 0.0)

    def _target_pos(self) -> Vec3 | None:
        return None

    def compute_angles(self, src: Vec3, dst: Vec3) -> tuple[float, float]:
        dx, dy, dz = dst.x - src.x, dst.y - src.y, dst.z - src.z
        yaw = math.degrees(math.atan2(dy, dx))
        pitch = math.degrees(math.atan2(dz, math.hypot(dx, dy)))
        return pitch, yaw

    def tick(self) -> None:
        if not self.cfg.aim.enabled:
            return
        target = self._target_pos()
        if not target:
            return
        pitch, yaw = self.compute_angles(self._local_pos(), target)
        smooth = max(self.cfg.aim.smooth, 1.0)
        # real write goes through view_matrix offset
        _ = (pitch / smooth, yaw / smooth)