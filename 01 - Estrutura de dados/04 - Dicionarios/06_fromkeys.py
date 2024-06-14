# FROMKEYS - cria chave em duas situações
# 1 - criar chaves e não colocar nenhum valor
# 2 - criar um conjuntos de chaves e coloca um valor padrão

resultado = dict.fromkeys(["nome", "telefone"])
print(resultado)  # {'nome': None, 'telefone': None}

print()

resultado = dict.fromkeys(["nome", "telefone"], "vazio")
print(resultado)  # {'nome': 'vazio', 'telefone': 'vazio'}
