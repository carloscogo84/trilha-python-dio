def exibir_mensagem():
    print("Olá mundo!")


exibir_mensagem()


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem_2("Luiz")
exibir_mensagem_2(nome="Carlos")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem_3()
exibir_mensagem_3("Pedro")
