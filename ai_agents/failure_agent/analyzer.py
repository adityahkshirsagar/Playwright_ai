"""
analyzer.py
===========

Extracts structured signals from raw failure payload.
"""

from typing import Dict


def analyze_failure(payload: Dict) -> Dict:
    error_type = payload.get("error_type", "").lower()
    error_message = payload.get("error_message", "").lower()

    # Check for locator issues first (more specific than timeout)
    if "locator" in error_message or "not found" in error_message:
        return {
            "failure_type": "LOCATOR_FAILURE",
            "summary": "Element locator not found.",
            "recommendation": "Switch to role-based or text-based selectors",
        }

    # Check for assertion issues
    if "assert" in error_message or "expect" in error_message:
        return {
            "failure_type": "ASSERTION_FAILURE",
            "summary": "Assertion mismatch detected.",
            "recommendation": "Verify expected data or application logic",
        }

    # Check for timeout issues (only if not a locator problem)
    if "timeout" in error_type or "timeout" in error_message:
        return {
            "failure_type": "TIMEOUT_FAILURE",
            "summary": "Test execution timed out.",
            "recommendation": "Add explicit waits or stabilize async dependencies",
        }

    return {
        "failure_type": "UNKNOWN_FAILURE",
        "summary": "Unclassified test failure.",
        "recommendation": "Manual investigation required",
    }

