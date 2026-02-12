*** Settings ***
Library     Browser
Library     Collections
Library     String
Library     ../libraries/Pages.py
Variables    ../resources/config.yaml

*** Keywords ***
# --- Given Steps ---
A product is added with manufacturer ${manufacturer} and model ${model}
    ${product}=    Create Dictionary    
    ...    manufacturer=${manufacturer}    
    ...    model=${model}    
    ...    number_in_stock=1    
    ...    price=1
    Pages.NavbarPage.Go To Product List
    Pages.ProductPage.Add New Product
    Pages.ProductAddPage.Add Product    ${product}
    Set Test Variable    ${ACTIVE_PRODUCT}    ${product}

An entry is added with manufacturer ${manufacturer} and model ${model}
    ${entry}=    Create Dictionary    
    ...    manufacturer=${manufacturer}    
    ...    model=${model}
    Pages.NavbarPage.Go To Watch List
    Pages.WatchListPage.Add New Entry
    Pages.WatchListAddPage.Add Entry    ${entry}

Fuzzy matching is enabled
    Pages.NavbarPage.Go To Product List
    Pages.ProductPage.Enable Fuzzy Matching

Standard matching is enabled
    Pages.NavbarPage.Go To Product List
    Pages.ProductPage.Enable Standard Matching

The product with manufacturer ${manufacturer} and model ${model} should be a standard match
    ${is_match}=    Pages.ProductPage.Is Product A Match    ${ACTIVE_PRODUCT}
    Should Be True    ${is_match}    msg=Expected a standard match for ${manufacturer} ${model}

The product with manufacturer ${manufacturer} and model ${model} should be a fuzzy match
    ${is_fuzzy}=    Pages.ProductPage.Is Product A Fuzzy Match    ${ACTIVE_PRODUCT}
    Should Be True    ${is_fuzzy}    msg=Expected a fuzzy match for ${manufacturer} ${model}

The product with manufacturer ${manufacturer} and model ${model} should not be a match
    ${is_match}=    Pages.ProductPage.Is Product A Match    ${ACTIVE_PRODUCT}
    ${is_fuzzy}=    Pages.ProductPage.Is Product A Fuzzy Match    ${ACTIVE_PRODUCT}
    Should Not Be True    ${is_match}    msg=Expected no standard match for ${manufacturer} ${model}
    Should Not Be True    ${is_fuzzy}    msg=Expected no fuzzy match for ${manufacturer} ${model}