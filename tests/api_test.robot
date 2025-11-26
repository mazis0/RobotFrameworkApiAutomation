*** Settings ***
Library    ../resources/ApiKeywords.py

*** Test Cases ***
Get Single User Successfully
    Given User id is    2
    When I request single user
    Then Response Status Should Be    200
    And Response Field Should Equal to    data.email    janet.weaver@reqres.in
    And Response Field Should Equal to    data.first_name    Janet
    And Response Field Should Equal to   data.last_name    Weaver

Create User Successfully
    Given I Create User with email and password    janet.weaver@reqres.in    Lion1234!
    When I send create user request
    Then Response Status Should Be    200
    And Response Field Should Equal    id    2
    And Response Field Should Equal    token    QpwL5tke4Pnpja7X2
