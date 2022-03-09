from Bank import Account
from robot.api.deco import keyword, library


class BankLibrary(object):
    ROBOT_LIBRARY_SCOPE = 'SUITE'
    """ library for showing the bank balance, Keeping an account of withdrwals and also
        deposits done in the bank. The functions of this library is defined in Bank.py 
        and also the libraries are imported from it"""

    def __init__(self):
        self.bank = Account()

    @keyword
    def accountnodisplay(self, name):
        """ Displays the Account number of the user from the Yaml Data"""

        self.bank.extractdata(name)
        return self.bank.getAccountno()

    @keyword
    def balancedisplay(self, name):
        """Displays the current and updated balance of the user.
        It shows the balance after withdrawal and deposit"""

        self.bank.extractdata(name)
        self.bal = self.bank.getbalance()
        self.bank.write_yaml(name)
        return self.bank.getbalance()

    @keyword
    def withdrwal(self, name, amount):
        """ It helps the user to withdraw the required amount from the bank.
        If the amount to be withdrawn exceeds the balance then an exception
        is raised and user is asked to enter a lesser amount """

        self.bank.extractdata(name)
        self.result = self.bank.withdraw(amount)
        self.bank.write_yaml(name)
        return self.result

    def deposit(self, name, deposit):
        """It helps the user to deposit the required amount to the bank
        It shows the updated balance after the deposit has been made"""
        self.bank.extractdata(name)
        self.result = self.bank.deposit(deposit)
        self.bank.write_yaml(name)
        return self.result



