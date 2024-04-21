class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def transfer_money(self, from_account, to_account, amount):
        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            return True
        else:
            return False

    def generate_statement(self, customer):
        for account in customer.accounts:
            print(f"Account Number: {account.account_number} and Balance: {account.balance}")
            print("------------------------")