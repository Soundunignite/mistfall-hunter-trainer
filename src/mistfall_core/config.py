"""Configuration model for the trainer."""
from dataclasses import dataclass, field
from pathlib import Path
import yaml


@dataclass
class AimConfig:
    enabled: bool = False
    fov: float = 45.0
    smooth: float = 3.5
    bone: str = "head"
    hotkey: str = "f1"


@dataclass
class ESPConfig:
    enabled: bool = False
    box: bool = True
    health_bar: bool = True
    distance: bool = True
    max_range: float = 350.0


@dataclass
class TrainerConfig:
    process_name: str = "MistfallHunter.exe"
    aim: AimConfig = field(default_factory=AimConfig)
    esp: ESPConfig = field(default_factory=ESPConfig)
    godmode: bool = False


def load_config(path: Path) -> TrainerConfig:
    if not path.exists():
        return TrainerConfig()
    raw = yaml.safe_load(path.read_text()) or {}
    cfg = TrainerConfig(process_name=raw.get("process_name", "MistfallHunter.exe"))
    aim = raw.get("aim", {})
    for k, v in aim.items():
        if hasattr(cfg.aim, k):
            setattr(cfg.aim, k, v)
    esp = raw.get("esp", {})
    for k, v in esp.items():
        if hasattr(cfg.esp, k):
            setattr(cfg.esp, k, v)
    cfg.godmode = bool(raw.get("godmode", False))
    return cfg