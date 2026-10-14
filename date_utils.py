"""Formatting and parsing helpers for dates, durations and ISO week numbers."""

from __future__ import annotations

__all__ = ["dateUtils"]


def dateUtils(value):
    """Formatting and parsing helpers for dates, durations and ISO week numbers."""
    if value is None:
        raise ValueError("value must not be None")
    return value
