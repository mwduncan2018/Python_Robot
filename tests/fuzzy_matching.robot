*** Settings ***
Documentation      Fuzzy matching indicates a match if either manufacturer or model match.
Resource           ../resources/base.resource
Resource           ../resources/matching_steps.resource
Test Setup         Browser Setup
Test Teardown      Browser Teardown
Test Tags          fuzzyMatching

*** Test Cases ***
Manufacturer match, model match
    [Template]    Standard Match Template
    # productManufacturer       productModel                    entryManufacturer       entryModel
    Wendys                      Taco Salad                      Wendys                  Taco Salad
    Wendys                      Apple Pecan Salad               Wendys                  Apple Pecan Salad
    Wendys                      Jalapeno Popper Salad           Wendys                  Jalapeno Popper Salad
    Wendys                      Bourbon Bacon Cheeseburger      Wendys                  Bourbon Bacon Cheeseburger

Manufacturer no match, model no match
    [Template]    No Match Template
    Taco Bell                   Grilled Cheese Burrito          Burger King             Impossible Whopper
    Taco Bell                   Veggie Burrito Supreme          Burger King             Texas Double Whopper
    Taco Bell                   Quesarito                       Burger King             Bacon King

Manufacturer match, model no match
    [Template]    Fuzzy Match Template
    Burger King                 Italian Original Chicken        Burger King             Four nuggets
    Burger King                 Spicy Chicken Sandwich          Burger King             Chicken Deluxe Sandwich

Manufacturer no match, model match
    [Template]    Fuzzy Match Template
    Popeyes                     Chicken Sandwich                Burger King             Chicken Sandwich
    McDonalds                   Hamburger                       Sonic                   Hamburger


*** Keywords ***
Standard Match Template
    [Arguments]    ${p_man}    ${p_mod}    ${e_man}    ${e_mod}
    A product is added with manufacturer ${p_man} and model ${p_mod}
    An entry is added with manufacturer ${e_man} and model ${e_mod}
    Fuzzy matching is enabled
    The product with manufacturer ${p_man} and model ${p_mod} should be a standard match

No Match Template
    [Arguments]    ${p_man}    ${p_mod}    ${e_man}    ${e_mod}
    A product is added with manufacturer ${p_man} and model ${p_mod}
    An entry is added with manufacturer ${e_man} and model ${e_mod}
    Fuzzy matching is enabled
    The product with manufacturer ${p_man} and model ${p_mod} should not be a match

Fuzzy Match Template
    [Arguments]    ${p_man}    ${p_mod}    ${e_man}    ${e_mod}
    A product is added with manufacturer ${p_man} and model ${p_mod}
    An entry is added with manufacturer ${e_man} and model ${e_mod}
    Fuzzy matching is enabled
    The product with manufacturer ${p_man} and model ${p_mod} should be a fuzzy match