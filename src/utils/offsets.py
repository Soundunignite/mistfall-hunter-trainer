"""Offset helpers for Mistfall Hunter 2026.01 build."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Offsets:
    local_player: int = 0x02A1B3C0
    entity_list: int = 0x02A1B420
    view_matrix: int = 0x02A2C010
    health: int = 0x1A8
    position: int = 0x2C0
    rotation: int = 0x2D8
    team: int = 0x318


OFFSETS_2026_01 = Offsets()


def get_offsets(build: str = "2026.01") -> Offsets:
    if build == "2026.01":
        return OFFSETS_2026_01
    raise ValueError(f"unknown build: {build}")