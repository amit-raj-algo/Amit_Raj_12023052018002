*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Verify API Response
    [Tags]    api    smoke

    Create Session    jsonplaceholder    https://jsonplaceholder.typicode.com
    ${response}=    GET On Session    jsonplaceholder    /posts/1

    Should Be Equal As Strings    ${response.status_code}    200