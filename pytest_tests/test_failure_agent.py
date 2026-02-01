from ai_agents.failure_agent import FailureAgent


def mock_ask_llm(prompt: str) -> str:
    """
    Mock LLM response used during pytest.
    """
    return "Mocked AI suggestion"


def test_locator_failure_suggests_fix(monkeypatch):
    # Mock the LLM call
    monkeypatch.setattr(
        "ai_agents.failure_agent.failure_agent.ask_llm",
        mock_ask_llm
    )

    payload = {
        "error_type": "TimeoutError",
        "error_message": "locator not found for #login-button",
        "spec_file": "login.spec.ts"
    }

    agent = FailureAgent()
    result = agent.analyze(payload)

    assert result["decision"] == "FIX_SUGGESTED"
    assert result["failure_type"] == "LOCATOR_FAILURE"
    assert result["confidence"] >= 0.7
    assert result["suggested_fix"]["ai_suggestion"] == "Mocked AI suggestion"


def test_timeout_failure_suggests_fix(monkeypatch):
    monkeypatch.setattr(
        "ai_agents.failure_agent.failure_agent.ask_llm",
        mock_ask_llm
    )

    payload = {
        "error_type": "TimeoutError",
        "error_message": "Test timed out after 30000ms",
        "spec_file": "checkout.spec.ts"
    }

    agent = FailureAgent()
    result = agent.analyze(payload)

    assert result["decision"] == "FIX_SUGGESTED"
    assert result["failure_type"] == "TIMEOUT_FAILURE"
    assert result["suggested_fix"]["ai_suggestion"] == "Mocked AI suggestion"


def test_assertion_failure_escalates(monkeypatch):
    """
    Assertion failures should escalate and NOT call LLM.
    """
    payload = {
        "error_type": "AssertionError",
        "error_message": "Expected value to be visible",
        "spec_file": "account.spec.ts"
    }

    agent = FailureAgent()
    result = agent.analyze(payload)

    assert result["decision"] == "ESCALATE"
    assert "suggested_fix" not in result


def test_unknown_failure_escalates(monkeypatch):
    payload = {
        "error_type": "UnknownError",
        "error_message": "Something weird happened",
        "spec_file": "unknown.spec.ts"
    }

    agent = FailureAgent()
    result = agent.analyze(payload)

    assert result["decision"] == "ESCALATE"
