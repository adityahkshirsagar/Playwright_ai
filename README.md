# Playwright AI Testing Framework

A Playwright-based UI automation framework built around Page Object Model (POM) patterns with AI-assisted failure analysis hooks. This repository is designed to showcase automation engineering skills: clean test structure, reporting, traceability, and maintainable page abstractions.

## Highlights

- Page Object Model (POM) architecture for maintainable tests
- Playwright configuration with trace, video, and screenshot capture
- HTML, JSON, and JUnit reporting
- Failure analysis pipeline (mock AI client) for structured debugging insights
- Clean test hooks and environment configuration

## Project Structure

- `playwright-tests/` Playwright project root
- `playwright-tests/tests/` Test specs
- `playwright-tests/pages/` Page objects
- `playwright-tests/hooks/` Shared hooks and test base
- `playwright-tests/fixtures/` Environment config
- `playwright-tests/utils/` Utilities (AI client, payload types)
- `docs/` High-level docs (placeholders)

## Tech Stack

- Playwright (TypeScript)
- Node.js
- npm

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

Edit:

- `playwright-tests/fixtures/env.ts`

This file controls base URL and credentials for the test environment. Avoid committing any real credentials.

## AI Failure Analysis (Mock)

On failure, the framework captures a screenshot and sends a structured payload to `utils/aiClient.ts`. The client currently returns a mock response and can be wired to a real service later.

## Skillset Demonstrated

- UI automation design with POM
- Robust Playwright configuration and reporting
- Test hooks, fixtures, and environment isolation
- Failure diagnostics (traces, screenshots, videos)
- Maintainable TypeScript test code

## Notes

- Tests target a public demo application.
- Headless is disabled by default in `playwright.config.ts`.

## License

Unspecified. Add a license if you plan to distribute publicly.
