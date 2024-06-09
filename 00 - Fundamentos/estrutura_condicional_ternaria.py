balance = 2000
withdraw = 2500

status = "Successful" if balance >= withdraw else "insufficient funds"

print(f"{status} withdrawal")
