# A forma mais comum de percorrer um dicionário é usando um FOR

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Essa forma funciona, mas não é a melhor
for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

print()

for chave, valor in contatos.items():  # .items() - retorna uma lista de tuplas
    print(chave, valor)
