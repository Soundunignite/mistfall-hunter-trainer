"""Mouse input adapter for aimbot smoothing."""
import ctypes
import time


class InputAdapter:
    def __init__(self) -> None:
        self._user32 = ctypes.windll.user32

    def move_relative(self, dx: int, dy: int) -> None:
        self._user32.mouse_event(0x0001, dx, dy, 0, 0)

    def smooth_move(self, dx: int, dy: int, steps: int = 8) -> None:
        sx, sy = dx // steps, dy // steps
        for _ in range(steps):
            self.move_relative(sx, sy)
            time.sleep(0.001)