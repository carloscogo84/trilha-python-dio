from abc import ABC, abstractmethod, abstractproperty

# OBS: Quando se tem um metodo abstrato, a classe torna-se abstrata e não pode mais ser instanciada diretamente.

# Com o conceito de contrato e classes abstratas, quando um metodo é abstrato a classe filha é obrigada a implementar


class ControleRemoto(ABC):  # extend
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTv(ControleRemoto):  # extend
    def ligar(self):
        print("Ligando a TV...")
        print("Ligando!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligando!")

    @property
    def marca(self):
        return "Sony"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando a AR...")
        print("Ligando!")

    def desligar(self):
        print("Desligando a AR...")
        print("Desligando!")

    @property
    def marca(self):
        return "LG"


# instanciar
controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
