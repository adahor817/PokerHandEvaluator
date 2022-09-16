from __future__ import annotations
"""Utilities."""
import random

def sample_cards(size: int) -> list[int]:
    """Sample random cards with size."""
    return random.sample(range(52), k=size)
