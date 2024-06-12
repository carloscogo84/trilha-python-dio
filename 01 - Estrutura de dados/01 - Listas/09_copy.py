# A lista e2 um objeto mutável, pra evitar que a lista seja alterada usa-se o copy
# copy retorna uma lista igual porém con a instancia diferente, ou seja não é a mesma lista

lista = [1, "Python", [40, 30, 20]]

lista_2 = lista.copy()

print(lista, lista_2)
print(id(lista), id(lista_2))

print()
print(lista)

lista_2[0] = 2
print(lista_2)
