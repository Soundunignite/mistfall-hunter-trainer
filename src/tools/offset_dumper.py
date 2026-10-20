"""Signature scanner — dumps resolved offsets to a JSON file."""
import json
import re
from pathlib import Path

import pymem
import pymem.pattern


def compile_pattern(pattern: str) -> bytes:
    return re.compile(pattern.replace(" ", "").replace("??", ".").encode())


def scan(process: str, module: str, pattern: str) -> int:
    pm = pymem.Pymem(process)
    base = pymem.process.module_from_name(pm.process_handle, module)
    raw = pm.read_bytes(base.lpBaseOfDll, base.SizeOfImage)
    rx = re.compile(pattern.replace(" ", "").replace("??", ".").encode())
    m = rx.search(raw)
    return base.lpBaseOfDll + m.start() if m else 0


def dump(process: str, module: str, out: Path) -> None:
    from src.mistfall_core.signatures import SIGNATURES
    results = {sig.name: scan(process, module, sig.pattern) for sig in SIGNATURES}
    out.write_text(json.dumps(results, indent=2))
    print(f"dumped {len(results)} offsets to {out}")