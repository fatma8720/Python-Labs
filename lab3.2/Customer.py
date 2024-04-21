class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def check_balance(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account.balance
        return "Account not found"