from playwright.sync_api import Page

from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.dashboard = DashboardToolbarViewComponent(page)
        self.student_chart_view = ChartViewComponent(page, 'students', 'bar')
        self.activities_chart_view = ChartViewComponent(page, 'activities', 'line')
        self.courses_chart_view = ChartViewComponent(page, 'courses', 'pie')
        self.scores_chart_view = ChartViewComponent(page, 'scores', 'scatter')

        self.courses_title = page.get_by_test_id('courses-widget-title-text')
        self.courses_chart = page.get_by_test_id('courses-pie-chart')

        self.scores_title = page.get_by_test_id('scores-widget-title-text')
        self.scores_chart = page.get_by_test_id('scores-scatter-chart')

