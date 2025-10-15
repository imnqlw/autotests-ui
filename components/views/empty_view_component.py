from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, '{identifier}-empty-view-icon', 'icon')
        self.title = Text(page, '{identifier}-empty-view-title-text', 'title')
        self.description = Text(page, '{identifier}-empty-view-description-text', 'description')

    def check_visible(self, identifier: str, title: str, description: str):
        # Проверяем видимость иконки
        self.icon.check_visible(identifier=identifier)

        # Проверяем видимость заголовка и его текст
        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)

        # Проверяем видимость описания и его текст
        self.description.check_visible(identifier=identifier)
        self.description.check_have_text(description, identifier=identifier)