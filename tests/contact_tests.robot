*** Settings ***
Documentation    Tests for the Contact page verification
Resource         ../resources/base.resource
Resource         ../resources/contact_steps.resource
Variables        ../resources/config.yaml
Test Tags       contact

Test Setup       Browser Setup
Test Teardown    Browser Teardown

*** Test Cases ***
Duncan Safe Product Footer
    The Contact page is viewed
    The following text should display in the footer    (Duncan Safe Product!)

GitHub Link
    The Contact page is viewed
    A GitHub link should be provided    https://github.com/mwduncan2018

Technical Skills
    When the Contact page is viewed
    Then the following skills should be listed
    ...    Robot
    ...    Playwright
    ...    Cypress
    ...    Appium
    ...    Selenium
    ...    Docker
    ...    JUnit
    ...    TestNG
    ...    pytest
    ...    pytest-bdd
    ...    SpecFlow
    ...    Cucumber
    ...    C# MVC
    ...    Java
    ...    Python
    ...    TypeScript
    ...    JavaScript
    ...    C#
    ...    Eggplant