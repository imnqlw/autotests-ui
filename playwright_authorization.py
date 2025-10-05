from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    email = page.get_by_test_id("registration-form-email-input").locator('input')
    email.fill('user.name@gmail.com')
    username = page.get_by_test_id("registration-form-username-input").locator('input')
    username.fill('username')
    password = page.get_by_test_id('registration-form-password-input').locator('input')
    password.fill('password')
    reg = page.get_by_test_id("registration-page-registration-button")
    reg.click()
    dashboard = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard).to_be_visible()




