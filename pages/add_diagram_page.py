from pages.base_page import BasePage

class addDiagramPage(BasePage):
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
        self.page.get_by_role("button", name="Save").click()
