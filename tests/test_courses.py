import pytest
from playwright.sync_api import sync_playwright, expect
import pytest

url_registration = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
url_courses = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
email = 'user.name@gmail.com'
name = 'username'
password = 'password'

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Скрипт открывает страницу регистрации.
        page.goto(url_registration)

        # Заполняет форму (Email, Username, Password) и нажимает Registration.
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # После успешного перехода сохраняет состояние браузера (storage state) в файл.
        context.storage_state(path="browser-state.json")

    # Создаётся новая сессия/контекст браузера с подстановкой сохранённого состояния.
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        # Открывается страница #/courses без повторной авторизации.
        page.goto(url_courses)

        # Проверяется наличие и текст заголовка “Courses”.
        course_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(course_title).to_have_text('Courses')

        # Проверяется наличие и видимость иконки пустого блока.
        icon_course = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_course).to_be_visible()

        # Проверяется наличие и текст блока “There is no results”.
        course_list = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(course_list).to_have_text('There is no results')

        # Проверяется наличие и текст описания блока: Results from the load test pipeline will be displayed here”.
        course_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(course_description).to_have_text('Results from the load test pipeline will be displayed here')