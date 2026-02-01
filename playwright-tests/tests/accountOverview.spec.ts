import { test, expect } from '../hooks/testBase';
import { LoginPage } from '../pages/LoginPage';
import { AccountOverviewPage } from '../pages/AccountOverviewPage';
import { env } from '../fixtures/env';

test.describe('Account Overview Tests', () => {
    test('should navigate to Account Overview after successful login', async ({ page }) => {
        const loginPage = new LoginPage(page);
        const accountOverviewPage = new AccountOverviewPage(page);

        await loginPage.login(env.credentials.username, env.credentials.password);
        await accountOverviewPage.navigateToAccountOverview();

        await expect(page).toHaveURL(/.*overview\.htm/);
        await expect(accountOverviewPage.getWelcomeMessage()).toBeVisible();
        await expect(accountOverviewPage.getAccountsOverviewHeading()).toBeVisible();
    });

    test('should display account table on Account Overview page', async ({ page }) => {
        const loginPage = new LoginPage(page);
        const accountOverviewPage = new AccountOverviewPage(page);

        await loginPage.login(env.credentials.username, env.credentials.password);
        await accountOverviewPage.navigateToAccountOverview();

        await expect(accountOverviewPage.getAccountTable()).toBeVisible();
        await expect(page.locator('table thead th:has-text("Account")')).toBeVisible();
        await expect(page.locator('table thead th:has-text("Balance*")')).toBeVisible();
        await expect(page.locator('table thead th:has-text("Available Amount")')).toBeVisible();
    });

    test('should display welcome message on Account Overview page', async ({ page }) => {
        const loginPage = new LoginPage(page);
        const accountOverviewPage = new AccountOverviewPage(page);

        await loginPage.login(env.credentials.username, env.credentials.password);
        await accountOverviewPage.navigateToAccountOverview();

        await expect(accountOverviewPage.getWelcomeMessage()).toBeVisible();
        await expect(accountOverviewPage.getWelcomeMessage()).toContainText('Welcome John Smith');
    });
});

