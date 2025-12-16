Feature: Language change on Home
  To validate multi-language support
  As a user
  I want to change the language from the dropdown

  Scenario: Change from English to Spanish
    Given I am on the language home page
    When I open the language dropdown
    And I select the language "Español"
    Then the current language should be "Español"
