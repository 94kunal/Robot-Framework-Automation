import sqlite3

class InsufficientBalance(ZeroDivisionError):
    def __init__(self, arg):
        self.msg = arg

class Database():

    def __init__(self):
        pass

    def create_database(self):

        self.conn = sqlite3.connect('Bank.db')
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE  Bank(
                          Account_no   Integer,
                          Balance   Integer,
                          Name text)""")

        self.conn.commit()
        self.conn.close()

    def create_account(self, account_no, balance, name):

        self.conn = sqlite3.connect('Bank.db')
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO Bank VALUES (?, ?, ?)", (account_no, balance, name))
        self.conn.commit()
        self.conn.close()

    def update_deposit(self, account_no, deposit):

        self.conn = sqlite3.connect('Bank.db')
        self.c = self.conn.cursor()
        self.dp = deposit
        self.balance = self.c.execute("SELECT * FROM Bank WHERE Account_no = (?)", (account_no,))
        items = self.c.fetchall()
        for item in items:
            self.balance = item[1]
        self.balance = int(self.balance) + int(self.dp)
        self.c.execute("UPDATE Bank SET Balance = (?) WHERE Account_no = (?)", (self.balance, account_no))
        self.conn.commit()
        self.conn.close()

    def update_withdrawl(self, account_no, withdraw):

        self.conn = sqlite3.connect('Bank.db')
        self.c = self.conn.cursor()
        self.wd = withdraw
        self.balance = self.c.execute("SELECT * FROM Bank WHERE Account_no = (?)", (account_no,))
        items = self.c.fetchall()
        for item in items:
            self.balance = item[1]
        try:
            if int(self.wd) > int(self.balance):
                raise InsufficientBalance("Insufficient Balance in the account")
            self.balance = int(self.balance) - int(self.wd)
            self.c.execute("UPDATE Bank SET Balance = (?) WHERE Account_no = (?)", (self.balance, account_no))

        except InsufficientBalance:
            print("Exception: Insufficient Balance in the account")

            while int(self.wd) > int(self.balance):
                print("Please enter a less amount")
                self.wd = int(input("Enter the amount to be withdrawn"))
            self.balance = int(self.balance) - int(self.wd)

        finally:

            self.c.execute("UPDATE Bank SET Balance = (?) WHERE Account_no = (?)", (self.balance, account_no))
            self.conn.commit()
            self.conn.close()

    def delete_account(self, account_no):

        self.conn = sqlite3.connect('Bank.db')
        self.c = self.conn.cursor()
        self.c.execute("DELETE from Bank WHERE Account_no =(?)", (account_no,))
        self.conn.commit()
        self.conn.close()

    def delete_database(self):

        self.conn = sqlite3.connect('Bank.db')
        self.c = self.conn.cursor()
        self.c.execute("DROP TABLE Bank")
        self.conn.commit()
        self.conn.close()

    def show_all(self):

        self.conn = sqlite3.connect('Bank.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT *FROM Bank")
        items = self.c.fetchall()
        self.conn.close()
        return items

