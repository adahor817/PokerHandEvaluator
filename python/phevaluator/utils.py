"""Utilities."""
import random
from __future__ import annotations

def sample_cards(size: int) -> list[int]:
    """Sample random cards with size."""
    return random.sample(range(52), k=size)
