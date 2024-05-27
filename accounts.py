class Account:
    def __init__(self, owner_name, account_number, initial_balance):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = initial_balance
        self.overdraft_limit = 0  
        self.minimum_balance = 0 

    def view_account_details(self):
        return f"Account Owner: {self.owner_name}\nAccount Number: {self.account_number}\nBalance: ksh{self.balance}"

    def change_account_owner(self, new_owner_name):
        self.owner_name = new_owner_name
        return f"Account owner updated to {new_owner_name}"

    def account_statement(self):
        return "Recent transactions:\nTransaction 1: -ksh50\nTransaction 2: +ksh100"

    def set_overdraft_limit(self, limit):
        self.overdraft_limit = limit
        return f"Overdraft limit set to ksh{limit}"

    def interest_calculation(self, rate):
        interest = self.balance * (rate / 100)
        self.balance += interest
        return f"Interest applied: ksh{interest}\nNew balance: ksh{self.balance}"

    def freeze_account(self):
        return "Account frozen"

    def unfreeze_account(self):
        return "Account unfrozen"

    def transaction_history(self):
        return "Transaction history:\nTransaction 1: -ksh50\nTransaction 2: +ksh100"

    def set_minimum_balance(self, min_balance):
        self.minimum_balance = min_balance
        return f"Minimum balance set to ksh{min_balance}"

    def transfer_funds(self, target_account, amount):
        return f"ksh{amount} transferred to account {target_account}"

    def close_account(self):
        return "Account closed successfully"


my_account = Account(owner_name="Staice", account_number="123456", initial_balance=5000)
print(my_account.view_account_details())
print(my_account.change_account_owner("Erin"))
print(my_account.account_statement())
print(my_account.set_overdraft_limit(500))
print(my_account.interest_calculation(2))
print(my_account.freeze_account())
print(my_account.unfreeze_account())
print(my_account.transaction_history())
print(my_account.set_minimum_balance(200))
print(my_account.transfer_funds(target_account="789012", amount=200))
print(my_account.close_account())
