# GET - outra forma de acessar valores dentro do dicionario

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Acessando desse jeito apresentará um jeito
# contatos["chave"]  # KeyError

# A maneira correta de acessar um valor que nåo sabe se é existente é usar o metodo GET

resultado = contatos.get("chave")  # none
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

# {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
resultado = contatos.get("guilherme@gmail.com", {})
print(resultado)
