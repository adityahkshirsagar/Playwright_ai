import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';

export class LoginPage extends BasePage {
    private readonly usernameInput: Locator;
    private readonly passwordInput: Locator;
    private readonly loginButton: Locator;

    constructor(page: Page) {
        super(page);
        this.usernameInput = page.locator('input[name="username"]');
        this.passwordInput = page.locator('input[name="password"]');
        this.loginButton = page.locator('input[value="Log In"]');
    }

    async login(username: string, password: string): Promise<void> {
        await this.usernameInput.fill(username);
        await this.passwordInput.fill(password);
        await this.loginButton.click();
        // Wait for navigation to complete (either overview for success or login for failure)
        await this.page.waitForURL(/.*(overview|login)\.htm/, { timeout: 10000 });
    }

    async navigateToLoginPage(baseUrl: string): Promise<void> {
        await this.page.goto(baseUrl);
    }
}

