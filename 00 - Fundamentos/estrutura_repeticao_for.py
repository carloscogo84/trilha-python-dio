text = input("Type a word: ")
vowels = "AEIOU"

# Exemplo utilizando um iterável
for letter in text:
    if letter.upper() in vowels:
        print(letter, end=" ")

print()  # Adds a line break

# Exemplo utilizando a função built-in-range
# start / stop / step
for number in range(0, 51, 5):
    print(number, end=" ")
