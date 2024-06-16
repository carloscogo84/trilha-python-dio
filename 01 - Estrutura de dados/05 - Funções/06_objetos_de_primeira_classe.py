def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


def subtrair(a, b):
    return a - b


def operacao(a, b):
    return a * 2 + b*3


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair)  # O resultado da operação 10 + 10 = 0
exibir_resultado(10, 10, operacao)  # O resultado da operação 10 + 10 = 50

operacao = somar

print(operacao(1, 23))
