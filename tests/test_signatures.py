"""Signature lookup sanity tests."""
from src.mistfall_core.signatures import by_name, SIGNATURES


def test_signature_count():
    assert len(SIGNATURES) >= 4


def test_lookup_local_player():
    sig = by_name("local_player", "2026.01")
    assert sig is not None
    assert "48 8B 05" in sig.pattern


def test_lookup_missing():
    assert by_name("nope", "2026.01") is None
    assert by_name("local_player", "1999.01") is None