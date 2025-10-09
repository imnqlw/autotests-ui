from playwright.sync_api import sync_playwright, expect

url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
email = 'user.name@gmail.com'
name = 'username'
password = 'password'

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    #Скрипт открывает страницу регистрации
    page.goto(url)

    #Скрипт проверяет, что кнопка Registration изначально находится в состоянии disabled.
    registration_button = page.get_by_test_id("registration-pages-registration-button")
    expect(registration_button).to_be_disabled()

    #Скрипт заполняет поля формы: Email, Username, Password.
    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill(email)

    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input.fill(name)

    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill(password)

    #После заполнения формы скрипт проверяет, что кнопка Registration перешла в состояние enabled.
    expect(registration_button).to_be_enabled()

