"""
rules.py
========

Deterministic rules controlling AI behavior.
"""

from typing import Dict


def should_escalate(signals: Dict) -> bool:
    """
    Decide whether this failure should be escalated.
    """

    if signals["failure_type"] == "ASSERTION_FAILURE":
        return True

    if signals["failure_type"] == "UNKNOWN_FAILURE":
        return True

    return False


def confidence_score(signals: Dict) -> float:
    """
    Assign confidence based on failure type.
    """

    scores = {
        "LOCATOR_FAILURE": 0.80,
        "TIMEOUT_FAILURE": 0.70,
        "ASSERTION_FAILURE": 0.60,
        "UNKNOWN_FAILURE": 0.40,
    }

    return scores.get(signals["failure_type"], 0.50)
