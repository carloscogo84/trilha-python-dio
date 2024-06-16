def salvar_carro(marca, modelo, ano, placa):
    # Salva o carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


print(salvar_carro("Fiat", "Palio", 1999, "ABC-1234"))
print(salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234"))
# Passando um dicionario para a função usando **
print(salvar_carro(**{"marca": "Fiat", "modelo": "Palio",
      "ano": 1999, "placa": "ABC-1234"}))
