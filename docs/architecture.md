# Mistfall Hunter Trainer — Architecture

Service-oriented layout:

- `src/bootstrap.py` — entry point, wires everything together.
- `src/mistfall_core/` — process, config, signatures, trainer facade.
- `src/services/` — aim, esp, godmode business logic.
- `src/handlers/` — hotkey + console event handlers (thin).
- `src/overlay/` — tk overlay HUD and ESP renderer.
- `src/adapters/` — pymem + input adapters (swappable for tests).
- `src/tools/` — signature scanner / offset dumper.
- `src/utils/` — logging, offsets.

## Data Flow

`bootstrap -> Trainer.attach() -> services -> overlay/handlers`
Each service reads from `GameProcess` and writes via `InputAdapter` or
`MemoryAdapter`. Adapters are Protocol-typed so tests can stub them.

## Adding a Feature

1. Add signature to `mistfall_core/signatures.py`.
2. Add offsets to `utils/offsets.py`.
3. Create service in `services/<feature>_service.py`.
4. Wire it into `Trainer.attach()`.
5. Add hotkey in `handlers/hotkey_handler.py`.