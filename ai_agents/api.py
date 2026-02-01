from fastapi import FastAPI, HTTPException
from orchestrator import route_request

app = FastAPI(
    title="AI Failure Analysis Service",
    version="1.0.0"
)

@app.post("/analyze-failure")
def analyze_failure(payload: dict):
    """
    Entry point for Playwright AI analysis.
    Receives failure payload and delegates to orchestrator.
    """
    try:
        if not payload:
            raise ValueError("Empty payload received")

        return route_request(payload)

    except Exception as exc:
        # IMPORTANT:
        # Do not swallow errors.
        # Let client decide fallback behavior.
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )