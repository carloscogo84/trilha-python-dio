# Loop infinito
while True:
    option = int(input("Type a number: "))

    if option == 10:
        break

    print(option)

for number in range(100):

    if number == 10:
        break

    print(number, end=" ")

print()


for number_1 in range(20):

    if number_1 == 15: # o numero 15 não foi exibido
        continue

    print(number_1, end=" ")
