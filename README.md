# Playwright AI Testing Framework

A Playwright-based UI automation framework built around Page Object Model (POM) patterns with AI-assisted failure analysis hooks. 

## Highlights

- Page Object Model (POM) architecture for maintainable tests
- Playwright configuration with trace, video, and screenshot capture
- HTML, JSON, and JUnit reporting
- Failure analysis pipeline (mock AI client) for structured debugging insights
- Agentic AI layer with a lightweight orchestrator and specialized agents
- Clean test hooks and environment configuration

## Project Structure

- `playwright-tests/` Playwright project root
- `playwright-tests/tests/` Test specs
- `playwright-tests/pages/` Page objects
- `playwright-tests/hooks/` Shared hooks and test base
- `playwright-tests/fixtures/` Environment config
- `playwright-tests/utils/` Utilities (AI client, payload types)
- `ai_agents/` Agentic framework (API, orchestrator, agents)
- `docs/` High-level docs (placeholders)

## Tech Stack

- Playwright (TypeScript)
- Node.js
- npm
- Python (FastAPI-based AI agent service)

## Quick Start

```bash
cd playwright-tests
npm install
```

## Running Tests

```bash
# Run all tests (headed by default)
npm test

# Run headed explicitly
npm run test:headed

# Clean current reports and run
npm run test:clean

# Clean current reports and run headed
npm run test:clean:headed
```

## Reports and Artifacts

Configured to capture:

- Traces (`trace: 'on'`)
- Screenshots on failure
- Videos on failure
- HTML report (`playwright-report/`)
- JSON and JUnit output (`test-results/`)

Results are archived after each run. The latest 5 archives are retained automatically.

## Environment Configuration

Create or update:

- `playwright-tests/fixtures/env.ts` (local only, not tracked)

This file controls the base URL and credentials for the test environment. Keep real credentials out of Git.

## Agentic Framework (AI Failure Analysis)

The `ai_agents/` package provides an agentic layer for analyzing test failures:

- `api.py` exposes a FastAPI endpoint for failure analysis requests
- `orchestrator/` routes payloads to a dedicated `FailureAgent`
- `failure_agent/` contains prompts, rules, and analysis logic
- Additional agents (healing, insight, optimization) are scaffolded for extension

The Playwright hook (`hooks/testBase.ts`) captures failure context and can be wired to this service.

## Skillset Demonstrated

- UI automation design with POM
- Robust Playwright configuration and reporting
- Test hooks, fixtures, and environment isolation
- Failure diagnostics (traces, screenshots, videos)
- Agentic AI workflow design and orchestration
- Maintainable TypeScript and Python test tooling

## Notes

- Tests target a public demo application.
- Headless is disabled by default in `playwright.config.ts`.

## License

MIT
