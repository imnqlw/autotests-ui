from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.input import Input
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.email_input = Input(page, 'registration-form-email-input', 'email')
        self.username_input = Input(page, 'registration-form-username-input', 'username')
        self.password_input = Input(page, 'registration-form-password-input', 'password')
        self.registration_button = Button(page, 'registration-page-registration-button', 'registration-button')



    def click_registration_button(self):
        self.registration_button.check_enabled()
        self.registration_button.click()