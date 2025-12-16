from behave import when
from pages.add_diagram_page import addDiagramPage

@when("I add the owner")
def step_impl(context):
    context.addDiagram = addDiagramPage(context.page)
    context.addDiagram.put_owner("QA")

@when("I add a description")
def step_impl(context):
    context.addDiagram.add_description("Testing the new model")

@when("I click on Add Diagram button")
def step_impl(context):
    context.addDiagram.click(context.addDiagram.add_button)

@when("I open dropdown")
def step_impl(context):
    context.addDiagram.open_dropdown()

@when("I select EoP" )
def step_impl(context):
    context.addDiagram.select_eop()

@when("I save the diagram" )
def step_impl(context):
    context.addDiagram.save_diagram()
