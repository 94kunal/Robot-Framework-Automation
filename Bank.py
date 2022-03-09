import yaml
import ruamel.yaml
import pathlib

class InsufficientBalance(ZeroDivisionError):
    def __init__(self, arg):
        self.msg = arg

class Account():

    def __init__(self):
        pass

    def withdraw(self, withdrawl):

        print()
        self.wd = withdrawl
        try:
            if self.wd > self.bal:
                raise InsufficientBalance("Insufficient Balance in the Account")
            self.bal = self.bal - self.wd
            return self.bal

        except InsufficientBalance:
            print("Exception: Insufficient Balance in the account")

            while self.wd > self.bal:
                print("Please enter a less amount")
                self.wd = int(input("Enter the amount to be withdrawn"))
            self.bal = self.bal - self.wd

        finally:
            print("The final Balance is", self.bal)

    def deposit(self, deposit):

        self.dp = deposit
        self.bal = self.bal + self.dp
        return self.bal

    def yaml_loadfile(self, filepath):

        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        return data

    def extractdata(self, name):

        filepath = pathlib.Path(__file__).parents[1].joinpath('Accounts.yaml')
        self.data = self.yaml_loadfile(filepath)
        items = self.data.get('Details')
        try:
            for i in range(0, len(items)):
                a = items[i].values()
                for key in a:
                    if name.upper() == key['name']:
                        self.Accno = key['Account no']
                        self.bal = key['Balance']
        except:
            print("Something is wrong")
            return False

    def write_yaml(self,name):

        filepath = pathlib.Path(__file__).parents[1].joinpath('Accounts.yaml')
        ruamel.yaml.util.load_yaml_guess_indent(open(filepath))
        data = self.data
        items = self.data['Details']

        for i in range(0, len(items)):
            a=items[i].values()
            for key in a:
                if name.upper() == key['name']:
                    key['Balance'] = self.bal

        with open(filepath, 'w') as fp:
            yaml.dump(data,fp)

    def getAccountno(self):
        return self.Accno

    def getbalance(self):
        return self.bal
