*** Settings ***
Library     Browser
Variables   ../resources/config.yaml

*** Keywords ***
Browser Setup
    New Browser    ${browser_options.name}    headless=${browser_options.headless}
    New Context    viewport={'width': 1280, 'height': 720}
    New Page       ${local.url}

Browser Teardown
    Take Screenshot
    Close Context    # Finalizes video and generates the link
    Close Browser