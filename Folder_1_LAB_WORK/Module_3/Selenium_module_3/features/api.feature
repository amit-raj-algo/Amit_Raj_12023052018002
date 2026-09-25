Feature: API Automation

  Scenario: Verify post API response
    Given the API client is initialized
    When I request post data using test case "TC001"
    Then the API response status should be 200