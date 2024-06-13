# A forma mais comum de acessar é usando um for

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# enumerate - para saber o indice

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
