# Conjuntos em python não suportam indexação e nem fatiamento.
# Caso necessita desses valores, precisa converter em uma lista

numeros = {1, 2, 3, 4}

numeros = list(numeros)  # Convertendo em uma lista
print(numeros[0])
