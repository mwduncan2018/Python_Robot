*** Settings ***
Documentation      Standard matching requires that both manufacturer and model match.
Resource           ../resources/base.resource
Resource           ../resources/matching_steps.resource
Test Setup         Browser Setup
Test Teardown      Browser Teardown
Test Tags          standardMatching

*** Test Cases ***
Manufacturer match, model match
    [Template]    Standard Match Template
    # productManufacturer    productModel    entryManufacturer    entryModel
    Porsche                  Cayenne         Porsche              Cayenne
    Porsche                  Boxster         Porsche              Boxster

Manufacturer no match, model no match
    [Template]    No Match Template
    Porsche                  911             Toyota               Corolla
    Porsche                  Cayman          Toyota               Camry

Manufacturer match, model no match
    [Template]    No Match Template
    Porsche                  Taycan          Porsche              Panamera
    Toyota                   Land Cruiser    Toyota               Supra

Manufacturer no match, model match
    [Template]    No Match Template
    BMW                      Sports Car      Tesla                Sports Car
    Honda                    SUV             General Motors       SUV


*** Keywords ***
Standard Match Template
    [Arguments]    ${p_man}    ${p_mod}    ${e_man}    ${e_mod}
    A product is added with manufacturer ${p_man} and model ${p_mod}
    An entry is added with manufacturer ${e_man} and model ${e_mod}
    Standard matching is enabled
    The product with manufacturer ${p_man} and model ${p_mod} should be a standard match

No Match Template
    [Arguments]    ${p_man}    ${p_mod}    ${e_man}    ${e_mod}
    A product is added with manufacturer ${p_man} and model ${p_mod}
    An entry is added with manufacturer ${e_man} and model ${e_mod}
    Standard matching is enabled
    The product with manufacturer ${p_man} and model ${p_mod} should not be a match