class Bicicleta:
    # Construtor
    # self - referência explicita para o objeto
    def __init__(self, cor, modelo, ano, valor):
        # Atributos da classe
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim, plim")

    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada")

    def correr(self):
        print("Vrummmmm....")

    # Representações de classe

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
b2.buzinar()
Bicicleta.buzinar(b2)  # Mesma coisa que a linha de cima
print(b2)
b2.correr()
