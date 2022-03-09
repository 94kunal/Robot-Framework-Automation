*** Settings ***

Library     BuiltIn
Resource    ../Keywords/Keywords.robot

*** Test Cases ***

Display Balance Details
    [Tags]                  bal
    Display Balance         ${name}

Display Account no
    [Tags]                  accno
    Display Account         ${name}

Display Amount after Deposit
    [Tags]                  depo
    Deposit Amount          ${name}             ${Amount}

Display Amount after Withdrawal
    [Tags]                  draw
    Withdraw Amount         ${name}             ${Amount}


