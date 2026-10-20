# Contributing to Mistfall Hunter Trainer

Thanks for your interest in improving the Mistfall Hunter Trainer. This project
is a community-driven, open-source trainer for the game *Mistfall Hunter*.
Contributions are welcome but please follow the guidelines below.

## Ground Rules

- This is **educational / modding-community software**. Do not use it on
  official servers or in competitive multiplayer.
- All pull requests must target the `dev` branch.
- Keep handlers thin — business logic belongs in `src/services/`.
- New memory signatures belong in `src/mistfall_core/signatures.py` and
  must include a version tag for the game build they were tested on.

## Development Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.bootstrap
```

## Submitting Changes

1. Fork and branch from `dev`.
2. Ensure `pytest tests/` passes.
3. Open a PR with a clear description of the feature and the game version
   it was validated against.

## Code Style

- Black + isort for Python.
- Type hints on all public functions.
- No bare `except:` clauses.