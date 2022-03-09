# Robot-Framework-Automation

This is an example to create keywords from python libraries and executing Test Cases through Robot Framework.

The example uses a Yaml file as Bank Account details and we have test cases to update, withdraw and view account details of different Account Holders.
The example alos includes a sqlite code which creates a database and We can create different accounts and update, withdraw or view details of different Account Holders.

All the Test cases are executed through robot framework.

**Prerequisites**

Please install the following python libraries to use and run the code:
  - ruamel.yaml, robotframework, robotframework-pabot 

**Steps For Running Test Cases**


All the commands should be run under Project directory

Note: For running commands in terminal to execute Test case:
    For Windows OS: use backword slash "\"
    For MacOS : use forward slas "/"

To run TestCases in parallel:
    ----> pabot --processes 2 --outputdir Results TestSuite\*.robot

Run Test Cases:

    To run all the Test cases at once:
        Go to the Test Case Folder and input command:
        ---->   robot -d Reports TestSuite\

    To run Test cases with Regular operations:
        ---->   robot -d Reports TestSuite\Test*.robot

    To run Individual Test:
        Go to the test Case Folder and input command:
        ----> robot -d Reports TestSuite\Test_Case.robot
        ----> robot -d Report_Database TestSuite\Test_Database.robot

    To run Parallel Test and to save Result of Parallel test execution in a specific folder:
        ----> pabot --processes 2 --outputdir Results TestSuite\*.robot

Running Banking Options

    Bank: A Bank with account details of various persons are created in Accounts.yaml.

    Test_Case.robot:

        To check the balance of a particular person we use the command:
        ----> robot -d Reports --variable name:kunal -i bal TestSuite\Test_Case.robot
              name options are: Kunal, Kushant, Keertika

        To Display the account no of a particular person we use the command
        ----> robot -d Reports --variable name:kunal -i accno TestSuite\Test_Case.robot
              name options are: Kunal, Kushant, Keertika

        To update the account of a particular person with a certain deposit amount.
        The changes after the Deposits are reflected back in Accounts.yaml file
        ----> robot -d Reports --variable name:kunal --variable Amount:1000 -i depo TestSuite\Test_Case.robot
              name options are: Kunal, Kushant, Keertika

        To update the account of a particular person with a certain withdrawal amount.
        The changes after the Deposits are reflected back in Accounts.yaml file
        ----> robot -d Reports --variable name:kunal --variable Amount:1000 -i draw TestSuite\Test_Case.robot
              name options are: Kunal, Kushant, Keertika

              Note: If withdrawal amount is greater than bank balance the person should enter less amount.

Running Database options:

    A bank Database can be created with the Account no, Balance and name of the Person
    Test_Database.robot

        To create a Database bank with the parameters: Account no, Balance, and name of the person.
        ----> robot -d Report_Database -i bank TestSuite\Test_Database.robot

        To create an Account inside the Database Bank.db
        ----> robot -d Report_Database --variable Account_no:450 --variable Amount:2000 --variable name:Kunal -i account TestSuite\Test_Database.robot
        name options: any text name
        Account_no options: any integer value
        Amount options: any integer value

        To show all Bank accounts in Database Bank.db
        ----> robot -d Report_Database -i show TestSuite\Test_Database.robot

        To deposit an amount to a particular bank account
        ----> robot -d Report_Database --variable Account_no:3201236 --variable Amount:2000 -i update TestSuite\Test_Database.robot
              To add amount to any account: Specify the account_no of the person already present in bank.db
                                            Specify the amount to be deposited

        To withdraw an amount from a particular bank account
        ----> robot -d Report_Database --variable Account_no:3201236 --variable Amount:2000 -i withdraw TestSuite\Test_Database.robot
              To withdraw amount from any account: Specify the account_no of the person already present in bank.db
                                                   Specify the amount to be withdrawn

        To delete an account of a Particular person from Database
        ----> robot -d Report_Database --variable Account_no:3201236 -i del TestSuite\Test_Database.robot

        To delete a table bank from the database
        ----> robot -d Report_Database -i delbank TestSuite\Test_Database.robot

