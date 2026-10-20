"""Simple REPL for runtime toggles during testing."""
from src.mistfall_core.trainer import Trainer


COMMANDS = {
    "aim": "toggle aimbot",
    "esp": "toggle esp",
    "god": "toggle godmode",
    "quit": "exit",
}


def run_console(trainer: Trainer) -> None:
    print("Mistfall Hunter Trainer console. Commands:", ", ".join(COMMANDS))
    while True:
        raw = input("> ").strip().lower()
        if raw == "quit":
            return
        if raw == "aim" and trainer.aim:
            trainer.cfg.aim.enabled = not trainer.cfg.aim.enabled
        elif raw == "esp" and trainer.esp:
            trainer.cfg.esp.enabled = not trainer.cfg.esp.enabled
        elif raw == "god" and trainer.god:
            trainer.cfg.godmode = not trainer.cfg.godmode
            if trainer.cfg.godmode:
                trainer.god.enable()
            else:
                trainer.god.disable()