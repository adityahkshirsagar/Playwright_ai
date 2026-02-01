import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';

export class AccountOverviewPage extends BasePage {
    private readonly welcomeMessage: Locator;
    private readonly accountsOverviewHeading: Locator;
    private readonly accountTable: Locator;
    private readonly logoutLink: Locator;

    constructor(page: Page) {
        super(page);
        this.welcomeMessage = page.locator('text=Welcome John Smith');
        this.accountsOverviewHeading = page.locator('h1:has-text("Accounts Overview")');
        this.accountTable = page.locator('table');
        this.logoutLink = page.locator('a:has-text("Log Out")');
    }

    async navigateToAccountOverview(): Promise<void> {
        await this.page.waitForURL(/.*overview\.htm/, { timeout: 10000 });
    }

    async clickLogout(): Promise<void> {
        await this.logoutLink.click();
        await this.page.waitForURL(/.*index\.htm/, { timeout: 10000 });
    }

    getWelcomeMessage(): Locator {
        return this.welcomeMessage;
    }

    getAccountsOverviewHeading(): Locator {
        return this.accountsOverviewHeading;
    }

    getAccountTable(): Locator {
        return this.accountTable;
    }

    getLogoutLink(): Locator {
        return this.logoutLink;
    }
}

