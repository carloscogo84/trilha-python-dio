def withdraw(amount: float):
    balance = 500

    if balance >= amount:
        print("amount drawn!")

    print("Thanks")


def deposit(amount: float):
    balance = 500
    balance += amount


withdraw(100)
print()
withdraw(1000)
