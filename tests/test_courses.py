from playwright.sync_api import expect
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

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

@pytest.mark.regression
@pytest.mark.courses
def test_create_course(create_course_page:CreateCoursePage, courses_list_page:CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form('', '', '', '0', '0')
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('testdata/files/image.png')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(title = "Playwright",
                                               estimated_time = "2 weeks",
                                               description = "Playwright",
                                               max_score = "100",
                                               min_score = "10")
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks")

