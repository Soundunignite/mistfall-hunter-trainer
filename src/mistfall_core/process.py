"""Thin wrapper around pymem for the Mistfall Hunter process."""
from typing import Optional
import pymem
import pymem.process


class GameProcess:
    def __init__(self, name: str) -> None:
        self.name = name
        self._pm: Optional[pymem.Pymem] = None

    def open(self) -> bool:
        try:
            self._pm = pymem.Pymem(self.name)
            return True
        except pymem.exception.ProcessNotFound:
            return False

    def module_base(self, module: str) -> int:
        assert self._pm is not None, "process not attached"
        mod = pymem.process.module_from_name(self._pm.process_handle, module)
        return mod.lpBaseOfDll if mod else 0

    def read_int(self, addr: int) -> int:
        assert self._pm is not None
        return self._pm.read_int(addr)

    def write_float(self, addr: int, value: float) -> None:
        assert self._pm is not None
        self._pm.write_float(addr, value)

    def close(self) -> None:
        if self._pm:
            self._pm.close_process()
            self._pm = None