"""Transparent overlay HUD rendered over Mistfall Hunter."""
import tkinter as tk

from src.mistfall_core.trainer import Trainer
from src.overlay.renderer import render_entities


class OverlayHUD:
    def __init__(self, trainer: Trainer) -> None:
        self.trainer = trainer
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", "black")
        self.root.configure(bg="black")
        self.root.geometry("1920x1080+0+0")
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

    def _tick(self) -> None:
        self.canvas.delete("all")
        if self.trainer.esp:
            render_entities(self.canvas, self.trainer.esp.collect())
        self.root.after(16, self._tick)

    def run(self) -> None:
        self.root.after(16, self._tick)
        self.root.mainloop()