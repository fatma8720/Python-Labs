from Bank import Bank
from Customer import Customer
from Account import Account

bank = Bank("MyBank")

customer1 = Customer("Fatma")
customer2 = Customer("Ali")



account1 = Account("1", 15000)
account2 = Account("2", 30500)

customer1.add_account(account1)
customer2.add_account(account2)

bank.add_customer(customer1)
bank.add_customer(customer2)

print("Before Transfer money : ")

bank.generate_statement(customer1)
bank.generate_statement(customer2)
print("After Transfer money")

bank.transfer_money(account1, account2, 573)

bank.generate_statement(customer1)
bank.generate_statement(customer2)
