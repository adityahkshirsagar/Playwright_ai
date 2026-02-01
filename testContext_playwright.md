# Test Context – Playwright Automation (ParaBank)

## Application Under Test
- ParaBank (Parasoft demo banking app)
- Base URL: https://para.testar.org/parabank/index.htm
- Public registration is disabled
- Use pre-seeded login users only

## Automation Style
- Use Playwright with TypeScript
- Follow Page Object Model (POM)
- Keep locators and actions inside page classes
- Keep assertions inside test files
- Use comments properly as and when needed

## Framework Rules
- Do not add AI logic
- Do not add lifecycle hooks unless explicitly asked
- Do not mix test logic into page classes
- Maintain saperate classes for every section.
- Maintain implemented reporting mechanism

## Scope
- Login
- Navigate to Account Overview
- Logout