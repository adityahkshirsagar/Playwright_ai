export interface AIFailurePayload {
    testName: string;
    status: 'failed';
    errorMessage?: string;
    stackTrace?: string;
    url?: string;
    retry?: number;
    screenshotPath?: string;
  }
  