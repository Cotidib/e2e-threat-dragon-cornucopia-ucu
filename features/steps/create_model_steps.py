from behave import given, when, then
from playwright.sync_api import sync_playwright
from pages.welcome_page import WelcomePage
from pages.home_page import HomePage

@given("I am on the home page")
def step_impl(context):
    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
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

