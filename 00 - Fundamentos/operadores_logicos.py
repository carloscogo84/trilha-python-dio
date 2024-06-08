# AND = To be true, everything has to be true
# OR = To be true, only one has to be true

print(True and True)  # True
print(True and False)  # False
print(True or True)  # True
print(True or False)  # True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

balance = 1000
withdraw = 250
overdraft_limit = 200
special_Account = True

expression = balance >= withdraw and withdraw <= overdraft_limit or special_Account and balance >= withdraw
print(expression)

expression_1 = (balance >= withdraw and withdraw <= overdraft_limit) or (
    special_Account and balance >= withdraw)
print(expression_1)

normal_account_sufficient_funds = (
    balance >= withdraw and withdraw <= overdraft_limit)
special_Account_sufficient_funds = (special_Account and balance >= withdraw)

expression_2 = normal_account_sufficient_funds or special_Account_sufficient_funds
print(expression_2)
