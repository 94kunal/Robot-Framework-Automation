from robot.api.deco import keyword, library
from BankDatabase import Database

class DatabaseLibrary(object):

    ROBOT_LIBRARY_SCOPE = 'SUITE'
    """ Library for showing the bank balance, keeping an account of withdrawls and also
        deposits done in the bank. The functions of this Library is defined in BankDatabse.py
        and all Libraries are imported from it"""

    def __init__(self):
        self.db = Database()

    def create_single_Accounts(self, account_no, balance, name):
        """It provides the option of creating a new Bank account with specifying the details
            of account no, balance and name"""
        self.db.create_account(account_no,balance, name)

    def update_deposits(self,account_no, deposit):
        """It updates the balance of account holders with the balance after deposit
            and checking the account no"""
        self.db.update_deposit(account_no, deposit)

    def show_database(self):
        """It shows the current users inside the database with Bank Details such
            as account no, Balance, None"""
        return self.db.show_all()

    def create_databases(self):
        """It creates a new SQLite database"""
        self.db.create_database()

    def delete_accounts(self, accountno):
        """It deletes an account from the database"""
        self.db.delete_account(accountno)

    def delete_databases(self):
        """It deletes the Table from the database"""
        self.db.delete_database()

    def update_withdrawls(self,account_no, withdraw):
        """It updates the balance of Account holders in the database after withdrawl"""
        self.db.update_withdrawl(account_no, withdraw)


