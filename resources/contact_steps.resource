*** Settings ***
Library     Browser
Library     String
Library     Collections
Library     ../libraries/Pages.py
Variables   ../resources/config.yaml

*** Keywords ***
The Contact page is viewed
    Pages.NavbarPage.Go To Contact

A GitHub link should be provided
    [Arguments]    ${expected_url}
    ${actual_url}=    Pages.ContactPage.Get GitHub Href
    ${expected_url}=    Strip String    ${expected_url}
    Should Be Equal    ${actual_url}    ${expected_url}    msg=GitHub URL does not match!

The following text should display in the footer
    [Arguments]    ${expected_text}
    ${actual_text}=    Pages.ContactPage.Get Footer Text
    ${expected_text}=    Strip String    ${expected_text}
    Should Contain    ${actual_text}    ${expected_text}    msg=Footer text did not contain: ${expected_text}

The following skills should be listed
    [Arguments]    @{expected_skills}
    ${actual_skills}=    Pages.ContactPage.Get All Skills
    
    FOR    ${skill}    IN    @{expected_skills}
        ${skill}=    Strip String    ${skill}
        List Should Contain Value    ${actual_skills}    ${skill}    msg=Expected skill '${skill}' was not found in the UI list: ${actual_skills}
    END