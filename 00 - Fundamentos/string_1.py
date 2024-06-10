# USEFUL STRING CLASS METHODS

name = "pYtHoN"

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

text = "   Hello World!   "

print(text + ".")
print(text.strip() + ".")  # Delete all spaces
print(text.rstrip() + ".")  # Deletes the spaces on the right
print(text.lstrip() + ".")  # Delete the spaces on the left

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))  # (14) string size
print(menu.center(20, "."))
print("-".join(menu))  # putting a dash in each letter
