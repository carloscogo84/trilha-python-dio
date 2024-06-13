# Difference - Tudo que tem em um conjunto que não tem no outro

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)  # {1}
print(resultado)

resultado = conjunto_b.difference(conjunto_a)  # {4}
print(resultado)
