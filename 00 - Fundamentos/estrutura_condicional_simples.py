of_legal_age = 18
special_age = 15

age = int(input("Enter your age: "))

if age >= of_legal_age:
    print("Older")

if age < of_legal_age:
    print("Under age")

print("--------------------")

if age >= of_legal_age:
    print("older")
else:
    print("Minor")

print("--------------------")

if age >= of_legal_age:
    print("Can drive")
elif (age >= special_age) and (age < of_legal_age):
    print("Provisional driving license")
else:
    print("Minor, cannot drive")
