from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage



class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)
        self.course_component = CreateCourseFormComponent(page)
        self.courses_tool_bar = CreateCourseToolbarViewComponent(page)
        self.exercises_tool_bar = CreateCourseExercisesToolbarViewComponent(page)
        self.courses_tool_bar_view = CreateCourseToolbarViewComponent(page)
        self.navbar = NavbarComponent(page)

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_estimated_time_input = (
            page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        )
        self.create_course_description_textarea = (
            page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        )
        self.create_course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')




    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')




    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible('create-course-exercises',
            'There is no exercises',
            'Click on "Create exercise" button to create new exercise'
        )
