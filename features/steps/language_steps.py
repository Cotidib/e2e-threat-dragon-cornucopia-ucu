from behave import given, when, then
from playwright.sync_api import sync_playwright
from pages.navbar_page import NavbarPage


@given("I am on the language home page")
def step_impl(context):
    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.navbar = NavbarPage(context.page)
    context.navbar.go_to("http://localhost:8080/")


@when("I open the language dropdown")
def step_impl(context):
    context.navbar.open_language_dropdown()


@when('I select the language "{language}"')
def step_impl(context, language):
    context.navbar.select_language(language)


@then('the current language should be "{language}"')
def step_impl(context, language):
    # Validate via the button text change
    context.page.wait_for_timeout(200)
    current = context.navbar.get_current_language_text()
    assert current.lower() == language.lower(), (
        f"Language did not change. Expected '{language}', got '{current}'"
    )
