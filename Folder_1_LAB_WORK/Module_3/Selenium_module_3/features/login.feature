#Feature: SauceDemo Login

  #Scenario: Validate login using external CSV test data

    #Given I open the SauceDemo login page
    #When I execute all login test cases from the CSV file
    #Then all login test cases should pass
    Feature: SauceDemo Login

  Scenario: Validate login using external CSV test data

    Given I open the SauceDemo login page
    When I execute all login test cases from the CSV file
    Then all login test cases should pass