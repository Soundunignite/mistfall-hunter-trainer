"""Memory signatures per game build. Update when Mistfall Hunter patches."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Signature:
    name: str
    pattern: str
    build: str


SIGNATURES = [
    Signature("local_player", "48 8B 05 ?? ?? ?? ?? 48 85 C0 74 0F", "2026.01"),
    Signature("entity_list", "48 8B 0D ?? ?? ?? ?? 48 8B 01 FF 50 40", "2026.01"),
    Signature("view_matrix", "F3 0F 10 05 ?? ?? ?? ?? F3 0F 11 45 80", "2026.01"),
    Signature("health_offset", "89 81 ?? ?? ?? ?? 8B 81 ?? ?? ?? ??", "2026.01"),
]


def by_name(name: str, build: str = "2026.01") -> Signature | None:
    for sig in SIGNATURES:
        if sig.name == name and sig.build == build:
            return sig
    return None