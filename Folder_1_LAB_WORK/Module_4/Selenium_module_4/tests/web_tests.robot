*** Settings ***
Resource    ../resources/common.robot

Test Setup       Open SauceDemo And Login
Test Teardown    Close Browser Session

*** Test Cases ***
Open Web Browser And Navigate
    [Tags]    web    smoke
    Page Should Contain Element    css=.title

Verify Login Page Element
    [Tags]    web
    Page Should Contain Element    id=inventory_container

Verify Successful Login
    [Tags]    web    smoke
    Page Should Contain    Products

Verify Expected Result
    [Tags]    web
    ${actual}=    Get Text    css=.title
    Should Be Equal As Strings    ${actual}    Products

Calculate Sum Using Custom Keyword
    [Tags]    custom
    ${result}=    Calculate Two Numbers    10    20
    Should Be Equal As Strings    ${result}    30.0

Use BuiltIn Mathematical Operation
    [Tags]    builtin
    ${result}=    Evaluate    10 + 20
    Should Be Equal As Integers    ${result}    30

Use String Library
    [Tags]    builtin
    ${text}=    Convert To Upper Case    robot framework
    Should Be Equal As Strings    ${text}    ROBOT FRAMEWORK