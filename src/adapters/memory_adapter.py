"""Low-level memory adapter — isolates pymem calls for testability."""
from typing import Protocol


class MemoryAdapter(Protocol):
    def read_int(self, addr: int) -> int: ...
    def write_float(self, addr: int, value: float) -> None: ...
    def read_bytes(self, addr: int, size: int) -> bytes: ...


class PymemAdapter:
    def __init__(self, pm) -> None:
        self._pm = pm

    def read_int(self, addr: int) -> int:
        return self._pm.read_int(addr)

    def write_float(self, addr: int, value: float) -> None:
        self._pm.write_float(addr, value)

    def read_bytes(self, addr: int, size: int) -> bytes:
        return self._pm.read_bytes(addr, size)