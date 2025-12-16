from pages.base_page import BasePage

class WelcomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.create_button = "//*[text()=' Create a new, empty threat model ']"
        