*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    String
Library    BuiltIn
Library    ../libraries/CustomKeywords.py

*** Variables ***
${URL}              https://www.saucedemo.com/
${USERNAME}         standard_user
${PASSWORD}         secret_sauce
${BROWSER}          chrome

*** Keywords ***
Open SauceDemo And Login
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id=user-name    10s
    Input Text    id=user-name    ${USERNAME}
    Input Password    id=password    ${PASSWORD}
    Click Button    id=login-button
    Wait Until Page Contains Element    css=.title    10s

Close Browser Session
    Close All Browsers

Calculate Two Numbers
    [Arguments]    ${number1}    ${number2}
    ${result}=    Calculate Sum    ${number1}    ${number2}
    RETURN    ${result}