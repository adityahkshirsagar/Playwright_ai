import { defineConfig, devices } from '@playwright/test';
import { env } from './fixtures/env';

export default defineConfig({
  testDir: './tests',

  use: {
    baseURL: env.baseUrl,
    headless: false,          // run headed by default; override with --headless if needed
    trace: 'on',              // always capture trace zips
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],

  reporter: [
    ['html', { outputFolder: 'playwright-report' }],
    ['json', { outputFile: 'test-results/results.json' }],
    ['junit', { outputFile: 'test-results/junit.xml' }],
    ['list'],
  ],

  outputDir: 'test-results/',
});
