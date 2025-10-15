from playwright.sync_api import Page, expect

from components.courses.course_view_component import CourseViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.empty_view = EmptyViewComponent(page, identifier="courses-list")
        self.course_view = CourseViewComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)

        # Заголовок и кнопка создания курса
        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        # Карточка курса
        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

        # Меню курса
        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')




    def check_visible_empty_view(self):
        self.empty_view.check_visible(identifier="courses-list",
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
                                      )


