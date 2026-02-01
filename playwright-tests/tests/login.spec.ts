import { env } from '../fixtures/env';
import { test, expect } from '../hooks/testBase';
import { LoginPage } from '../pages/LoginPage';

test.describe('Login Tests', () => {

  test('should successfully login with valid credentials', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.login(env.credentials.username, env.credentials.password);

    await expect(page).toHaveURL(/.*overview\.htm/);
    await expect(page.locator('text=Welcome John Smith')).toBeVisible();
  });

  test('should fail login with invalid username', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.login('invalid_user', 'demo');

    await expect(page).toHaveURL(/.*login\.htm/);
    await expect(page.locator('text=The username and password could not be verified.')).toBeVisible();
  });

  test('should fail login with invalid password', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.login('john', 'wrong_password');

    await expect(page).toHaveURL(/.*login\.htm/);
    await expect(page.locator('text=The username and password could not be verified.')).toBeVisible();
  });

  test('should fail login with empty credentials', async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.login('', '');

    await expect(page).toHaveURL(/.*login\.htm/);
  });

  test('should display login form elements', async ({ page }) => {
    await expect(page.locator('input[name="username"]')).toBeVisible();
    await expect(page.locator('input[name="password"]')).toBeVisible();
    await expect(page.locator('input[value="Log In"]')).toBeVisible();
  });

});