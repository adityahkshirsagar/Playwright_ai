"""
orchestrator.py
===============

Thin dispatcher between API layer and AI agents.

Responsibilities:
- Accept failure payload from API
- Delegate analysis to FailureAgent
- Return structured decision

NO business logic lives here.
"""

from typing import Dict
from ai_agents.failure_agent import FailureAgent



def route_request(payload: Dict) -> Dict:
    """
    Entry point called by API layer.

    Args:
        payload (dict): Failure payload from Playwright / CI

    Returns:
        dict: Structured AI decision
    """

    agent = FailureAgent()
    return agent.analyze(payload)
