*** Settings ***

Library     ../Banking/BankLibrary.py
Library     BuiltIn

Variables   ../Variables/Variables.py       name        Amount

*** Keywords ***

Display Account
    [Arguments]                 ${name}
    ${Account_no}               AccountNo Display       ${name}
    LOG TO CONSOLE              ${Account_no}

Display Balance
    [Arguments]                 ${name}
    ${balance}=                 Balance Display         ${name}
    log to console              ${balance}

Deposit Amount
    [Arguments]                 ${name}                 ${deposit_amount}
    ${deposit}                  convert to integer      ${deposit_amount}
    ${Amount}=                  Deposit                 ${name}             ${deposit}
    LOG TO CONSOLE              ${Amount}

Withdraw Amount
    [Arguments]                 ${name}                 ${withdraw_amount}
    ${withdraw}                 convert to integer      ${withdraw_amount}
    ${Amount}=                  withdrwal               ${name}             ${withdraw}
    LOG TO CONSOLE              ${Amount}



