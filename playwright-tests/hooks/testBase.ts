// hooks/testBase.ts

import { test as base, expect } from '@playwright/test';
import { AIClient } from '../utils/aiClient';
import { AIFailurePayload } from '../utils/aiPayload';
import { env } from '../fixtures/env';

export const test = base.extend({});

const aiClient = new AIClient();

test.beforeAll(async () => {
  console.log('=== Test Suite Started ===');
});

test.beforeEach(async ({ page }) => {
  // Only navigation — nothing page-specific
  await page.goto(env.baseUrl, { waitUntil: 'domcontentloaded' });
});

test.afterEach(async ({ page }, testInfo) => {
  if (testInfo.status === 'failed') {
    const screenshotPath = testInfo.outputPath('failure.png');

    await page.screenshot({ path: screenshotPath });

    const payload: AIFailurePayload = {
      testName: testInfo.title,
      status: 'failed',
      errorMessage: testInfo.error?.message,
      stackTrace: testInfo.error?.stack,
      url: page.url(),
      retry: testInfo.retry,
      screenshotPath,
    };

    await aiClient.analyzeFailure(payload);
  }
});

test.afterAll(async () => {
  console.log('=== Test Suite Finished ===');
});

export { expect };