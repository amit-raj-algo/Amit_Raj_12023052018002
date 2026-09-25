Feature: Data Driven Login

  Scenario Outline: Login using different credentials
    Given I open the SauceDemo login page
    When I login with username "<username>" and password "<password>"
    Then the login result should be "<result>"

    Examples:
      | username      | password     | result  |
      | standard_user | secret_sauce | success |
      | standard_user | wrong_pass   | error   |
      | wrong_user    | secret_sauce | error   |