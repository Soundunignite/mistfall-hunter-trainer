"""Global hotkey dispatch for trainer toggles."""
import logging
from typing import Callable, Dict
import keyboard

from src.mistfall_core.config import TrainerConfig


class HotkeyHandler:
    def __init__(self, cfg: TrainerConfig) -> None:
        self.cfg = cfg
        self.log = logging.getLogger("mistfall.hotkeys")
        self._bindings: Dict[str, Callable[[], None]] = {}

    def bind(self, key: str, action: Callable[[], None]) -> None:
        self._bindings[key.lower()] = action
        keyboard.add_hotkey(key, self._wrap(key, action))

    def _wrap(self, key: str, action: Callable[[], None]) -> Callable[[], None]:
        def _inner() -> None:
            self.log.debug("hotkey fired: %s", key)
            action()
        return _inner

    def start(self) -> None:
        keyboard.wait()