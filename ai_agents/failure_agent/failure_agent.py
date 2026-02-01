"""
failure_agent.py
================

Primary AI agent responsible for analyzing Playwright test failures
and producing a structured decision.

This class coordinates:
- signal analysis
- rule evaluation
- AI prompting (future)
"""

from typing import Dict

from .analyzer import analyze_failure
from .rules import should_escalate, confidence_score
from .prompt_templates import LOCATOR_PROMPT, TIMEOUT_PROMPT
from ai_agents.llm_client import ask_llm
from .prompt_templates import LOCATOR_PROMPT, TIMEOUT_PROMPT 


class FailureAgent:
    """
    Public entry point for failure analysis.
    """

    def analyze(self, payload: Dict) -> Dict:
        """
        Analyze a Playwright failure payload and return a decision.
        """

        signals = analyze_failure(payload)

        if should_escalate(signals):
            return self._escalate(payload, signals)

        return self._suggest_fix(payload, signals)

    # -------------------------------------------------

    def _suggest_fix(self, payload: Dict, signals: Dict) -> Dict:
        llm_suggestion = None
        if signals["failure_type"] == "LOCATOR_FAILURE":
            llm_suggestion = ask_llm(LOCATOR_PROMPT + f"\nError: {payload.get('error_message')}")
        elif signals["failure_type"] == "TIMEOUT_FAILURE":
            llm_suggestion = ask_llm(TIMEOUT_PROMPT + f"\nError: {payload.get('error_message')}")
        return {
        "decision": "FIX_SUGGESTED",
        "agent": "FailureAgent",
        "failure_type": signals["failure_type"],
        "confidence": confidence_score(signals),
        "summary": signals["summary"],
        "suggested_fix": {
            "file": payload.get("spec_file"),
            "recommendation": signals["recommendation"],
            "ai_suggestion": llm_suggestion,
        },
    }


    def _escalate(self, payload: Dict, signals: Dict) -> Dict:
        """
        Escalate failure to human / CI.
        """

        return {
            "decision": "ESCALATE",
            "agent": "FailureAgent",
            "failure_type": signals["failure_type"],
            "confidence": confidence_score(signals),
            "summary": signals["summary"],
            "reason": "Rule-based escalation triggered",
        }
