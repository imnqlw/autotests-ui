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
def test_empty_courses_list(chromium_page_with_state):

    chromium_page_with_state.goto(url_courses)
    # Проверяется наличие и текст заголовка “Courses”.
    course_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_title).to_have_text('Courses')

    # Проверяется наличие и видимость иконки пустого блока.
    icon_course = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_course).to_be_visible()

    # Проверяется наличие и текст блока “There is no results”.
    course_list = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(course_list).to_have_text('There is no results')

    # Проверяется наличие и текст описания блока: Results from the load test pipeline will be displayed here”.
    course_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(course_description).to_have_text('Results from the load test pipeline will be displayed here')
