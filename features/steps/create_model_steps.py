from behave import given, when, then
from playwright.sync_api import sync_playwright
from pages.welcome_page import WelcomePage
from pages.home_page import HomePage
from pages.create_model_page import CreateModelPage

@given("I am on the home page")
def step_impl(context):
    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page(accept_downloads=True)
    context.page.add_init_script("delete window.showSaveFilePicker")
    context.home_page = HomePage(context.page)
    context.home_page.go_to("http://localhost:8080/")

@when("I click on Login button")
def step_impl(context):
    context.home_page = HomePage(context.page)
    context.home_page.click(context.home_page.login_button)

@when("I click on Create button")
def step_impl(context):
    context.welcome_page = WelcomePage(context.page)
    context.welcome_page.click(context.welcome_page.create_button)    

@when("I add the owner")
def step_impl(context):
    context.create_model = CreateModelPage(context.page)
    context.create_model.put_owner("QA")

@when("I add a description")
def step_impl(context):
    context.create_model.add_description("Testing the new model")

@when("I click on Add Diagram button")
def step_impl(context):
    context.create_model.click(context.create_model.add_button)

@when("I open dropdown")
def step_impl(context):
    context.create_model.open_dropdown()

@when("I select EoP" )
def step_impl(context):
    context.create_model.select_eop()

@when("I save the diagram" )
def step_impl(context):
    context.create_model.save_diagram()
