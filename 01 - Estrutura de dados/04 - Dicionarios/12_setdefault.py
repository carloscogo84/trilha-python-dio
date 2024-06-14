# SETDEFAULT - Se o atributo nao estiver no dicionario, ele adiciona com o valor que vc colocou.
# Se o valor existir no dicionario, retorna o valor existente

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
