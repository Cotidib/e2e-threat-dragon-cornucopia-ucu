Feature: Add Component

Scenario: Successful new model
    Given I am on the home page
    When I click on Login button
    When I click on ' Open an existing threat model ' button
    When I click on Open button
    When I upload a model
    When I click on 'New EoP Diagram'
    When I drag an Actor component
    When I drop an Actor component
    Then the Actor component stays on the canvas

