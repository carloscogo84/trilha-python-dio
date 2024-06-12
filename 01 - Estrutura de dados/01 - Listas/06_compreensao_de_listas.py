# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]

# primeiro o Python itera e atribui cada item pra variavel numero, atens de retornar verifica a condição
#        Retorno /    iteracao       /   Condição
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
