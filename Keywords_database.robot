*** Settings ***

Library         ../Database_Bank/DatabaseLibrary.py
Library         BuiltIn
Variables       ../Variables/Variables.py           name        Amount      Account_no

*** Keywords ***

Create a Bank Database

    create databases

Open a Bank Account

    [Arguments]                     ${Account_no}           ${Amount}           ${name}
    Create single Accounts          ${Account_no}           ${Amount}           ${name}

Show Accounts

    ${Details}                      show database
    LOG TO CONSOLE                  ${Details}

Update Account After Deposit

     [Arguments]                    ${Account_no}          ${Amount}
     Update deposits                ${Account_no}          ${Amount}

Update Account After Withdrawl

     [Arguments]                    ${Account_no}          ${Amount}
     Update Withdrawls              ${Account_no}          ${Amount}

Delete an Account

     [Arguments]                    ${Account_no}
     Delete Accounts                ${Account_no}

Delete a Bank Database

    delete databases







