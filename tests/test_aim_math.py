"""Unit tests for aim angle math."""
import math
from src.services.aim_service import AimService, Vec3
from src.mistfall_core.config import TrainerConfig


def make_svc() -> AimService:
    return AimService(proc=None, cfg=TrainerConfig())  # type: ignore[arg-type]


def test_angles_north():
    svc = make_svc()
    pitch, yaw = svc.compute_angles(Vec3(0, 0, 0), Vec3(0, 10, 0))
    assert abs(yaw - 90.0) < 1e-6
    assert abs(pitch - 0.0) < 1e-6


def test_angles_east():
    svc = make_svc()
    pitch, yaw = svc.compute_angles(Vec3(0, 0, 0), Vec3(10, 0, 0))
    assert abs(yaw - 0.0) < 1e-6


def test_angles_diag():
    svc = make_svc()
    pitch, yaw = svc.compute_angles(Vec3(0, 0, 0), Vec3(1, 1, 1))
    assert abs(yaw - 45.0) < 1e-6
    assert pitch > 0