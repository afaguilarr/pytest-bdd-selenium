@API
Feature: Todo API

  Scenario: Creating a todo
    When the user makes an example API call
    Then the API responds successfully
    And the response body contains the expected data