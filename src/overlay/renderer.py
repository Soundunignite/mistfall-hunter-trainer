"""Draw ESP boxes and labels on the overlay canvas."""
import tkinter as tk
from typing import List

from src.services.esp_service import ESPEntity


def render_entities(canvas: tk.Canvas, entities: List[ESPEntity]) -> None:
    for e in entities:
        x, y = int(e.x), int(e.y)
        canvas.create_rectangle(x - 25, y - 60, x + 25, y, outline="#00ff88", width=2)
        canvas.create_text(x, y - 70, text=f"{e.name} [{e.health}hp]",
                           fill="#00ff88", font=("Consolas", 9))
        canvas.create_text(x, y + 12, text=f"{e.distance:.0f}m",
                           fill="#ffd700", font=("Consolas", 8))