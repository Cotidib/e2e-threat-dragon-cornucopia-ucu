Feature: Create Model

  Scenario: Successful new model
    Given I am on the home page
    When I click on Login button
    And I click on Create button
    And I add the owner
    And I add a description
    And I click on Add Diagram button
    And I open dropdown
    And I select EoP
    And I save the diagram