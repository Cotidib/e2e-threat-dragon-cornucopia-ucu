from pages.base_page import BasePage
import os

class CreateModelPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_button = "//*[text()=' Add a new diagram... ']"
        
    def put_owner(self, owner):
        self.page.get_by_label("Owner").fill(owner)

    def add_description(self, description):
        self.page.get_by_label("description").fill(description)

    def open_dropdown(self):
        self.page.get_by_role("button", name="STRIDE").click()

    def select_eop(self):
        self.page.get_by_role("menuitem", name="EoP").click()

    def save_diagram(self):
        os.makedirs("downloads", exist_ok=True)
        with self.page.expect_download() as download_info:
            self.page.get_by_role("button", name="Save").click()
        download = download_info.value
        download.save_as("downloads/test-diagram.json")
