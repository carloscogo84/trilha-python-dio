balance = 1000
overdraft_limit = 500

# Do they occupy the same region of memory?
print(balance is overdraft_limit)  # False
print(balance is not overdraft_limit)  # True
