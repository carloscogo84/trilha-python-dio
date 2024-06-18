class Cachorro:

    # O init sempre é executado quando uma instancia objeto é criado
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Destroi o objeto / Executado no final
    def __del__(self):
        print("removendo a intância da classe")

    def latir(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")

c.latir()

# Forçando o DEL
print("Olá mundo")
print("Olá mundo")

del c
print("Olá mundo")
print("Olá mundo")

# criar_cachorro()
