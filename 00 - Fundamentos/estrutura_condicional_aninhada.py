normal_account = False
university_account = False
balance = 2000
withdraw = 1500
overdraft = 450

if normal_account:
    if balance > withdraw:
        print("Successful withdrawal")
    elif withdraw <= (balance + overdraft):
        print("Successful withdrawal using overdraft")
    else:
        print("Unable to withdraw, insufficient funds")

elif university_account:
    if balance >= withdraw:
        print("Successful withdrawal")
    else:
        print("insufficient funds")
else:
    print("Invalid account")
