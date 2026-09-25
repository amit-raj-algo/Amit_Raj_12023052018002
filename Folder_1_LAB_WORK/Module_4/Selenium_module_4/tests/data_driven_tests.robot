*** Settings ***
Library    SeleniumLibrary
Library    ../libraries/CustomKeywords.py

*** Variables ***
${URL}       https://www.saucedemo.com/
${BROWSER}   chrome

*** Test Cases ***
Data Driven Login Test
    [Tags]    data-driven    web

    ${test_data}=    Read Login Data    ${EXECDIR}/data/login_data.csv

    FOR    ${row}    IN    @{test_data}
        ${username}=    Set Variable    ${row}[0]
        ${password}=    Set Variable    ${row}[1]
        ${expected}=    Set Variable    ${row}[2]

        Open Browser    ${URL}    ${BROWSER}
        Maximize Browser Window

        Wait Until Element Is Visible    id=user-name    10s
        Input Text    id=user-name    ${username}
        Input Password    id=password    ${password}
        Click Button    id=login-button

        Run Keyword If    '${expected}' == 'Products'
        ...    Verify Successful Login

        Run Keyword If    '${expected}' != 'Products'
        ...    Verify Failed Login    ${expected}

        Close All Browsers
    END

*** Keywords ***
Verify Successful Login
    Wait Until Page Contains Element    css=.title    10s
    Page Should Contain    Products

Verify Failed Login
    [Arguments]    ${expected_message}
    Wait Until Page Contains Element    css=h3[data-test="error"]    10s
    ${actual_message}=    Get Text    css=h3[data-test="error"]
    Should Contain    ${actual_message}    ${expected_message}
