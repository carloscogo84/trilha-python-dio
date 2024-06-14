contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# retira os itens na sequencia
resultado = contatos.popitem()
# ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# se estiver vazio apresenta um key error
# resultado = contatos.popitem()
# print(resultado)
