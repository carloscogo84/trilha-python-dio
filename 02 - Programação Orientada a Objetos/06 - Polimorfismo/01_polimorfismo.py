class Passaro:
    def voar(self):
        print("Voando....")

# Herança


class Pardal(Passaro):
    def voar(self):
        super().voar()

# Herança


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# Conceito de polimorfismo está aqui
# Recebe um objeto e se comporta de varias formas diferentes, porem chamando o mesmo metodo


def plano_voo(objeto):
    objeto.voar()


pardal = Pardal()
avestruz = Avestruz()

plano_voo(pardal)
plano_voo(avestruz)

print()

plano_voo(Pardal())
plano_voo(Avestruz())
