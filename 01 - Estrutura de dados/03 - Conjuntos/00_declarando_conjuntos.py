# SET - Não possui objetos repetidos, usado para eliminar elementos repetidos
# Não garante a ordem

numeros = set([1, 2, 3, 1, 3, 4])  # {1, 2, 3, 4}
print(numeros)

letras = set("abacaxi")  # {'b', 'i', 'a', 'x', 'c'}
print(letras)

carros = set(("palio", "gol", "celta", "palio"))  # {'palio', 'celta', 'gol'}
print(carros)


linguagens = {"Python", "java", "Python"}  # Sintaxe não muito usada
print(linguagens)  # {'Python', 'java'}
