numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)  # Se passar um valor que existe ele descarta
numeros.discard(45)  # Se não houver, não apresenta erro

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
