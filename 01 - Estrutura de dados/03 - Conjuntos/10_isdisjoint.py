# isdisjoint
# Conjunto dijunto - Conjunto onde não se tocam

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# True - Não tem intersecção entre eles
resultado = conjunto_a.isdisjoint(conjunto_b)
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)
