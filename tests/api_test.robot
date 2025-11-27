*** Settings ***
Library    ../resources/ApiKeywords.py

*** Test Cases ***
Get Single User Successfully
    Given User id is 2
    When I request single user
    Then Response status should be 200
    And Response key "data.email" should equal to value "janet.weaver@reqres.in"
    And Response key "data.first_name" should equal to value "Janet"
    And Response key "data.last_name" should equal to value "Weaver"


Create User Successfully
    Given I create user with email "janet.weaver@reqres.in" and password "Lion1234!"
    When I send create user request
    Then Response status should be 200
    And Response key "id" should equal to value "2"
    And Response key "token" should equal to value "QpwL5tke4Pnpja7X2"
    
    
*** Keywords ***
User id is ${users}
    Given User id is    ${users}
Response status should be ${response} 
    Then Response Status Should Be    ${response} 
Response key "${key}" should equal to value "${value}"
    And Response Field Should Equal to    ${key}    ${value}
I create user with email "${email}" and password "${password}"  
    Given I Create User with email and password    ${email}    ${password}