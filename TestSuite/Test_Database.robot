*** Settings ***

Library     BuiltIn
Resource    ../Keywords/Keywords_database.robot

*** Test Cases ***

Setting up a Database
    [Tags]                              bank
    Create a Bank Database

Create a Bank Account
    [Tags]                              account
    Open a Bank Account                 ${Account_no}           ${Amount}           ${name}

Show Bank Accounts
    [Tags]                              show
    Show Accounts

Save a Deposit Amount
    [Tags]                              update
    Update Account After Deposit        ${Account_no}          ${Amount}

Save a Withdrawal Amount
    [Tags]                              withdraw
    Update Account After Withdrawl      ${Account_no}          ${Amount}

Delete an Account from Database
    [Tags]                              del
    Delete an Account                    ${Account_no}

Deleting a Database
    [Tags]                              delbank
    Delete a Bank Database


