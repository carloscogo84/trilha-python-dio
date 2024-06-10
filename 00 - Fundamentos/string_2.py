# INTERPOLATION OF VARIABLES

name = "Carlos"
age = 40
occupation = "Programer"
program = "Python"
balance = 45.435

print("name: %s age: %d" % (name, age))  # 1
print("name: {} age: {}".format(name, age))  # 2
print("name: {1} age: {0}".format(age, name))  # 2
print("name: {1} age: {0} name: {1} {1}".format(age, name))  # 2
print("name: {name} age: {age}".format(name=name, age=age))  # 2

data = {"name": "Carlos", "age": 40}

print("name: {name} age: {age}".format(**data))

print(f"name: {name} age: {age}")  # Most commonly used
print(f"name: {name} age: {age} balance {balance}")
print(f"name: {name} age: {age} balance {balance:.2f}")
