class Foo:
    # Contrutor de inicializacao
    def __init__(self, x=None):
        self._x = x

    # Propriedade pega um metodo e transforma em uma propriedade
    # Para retornar valor, precisa ter o property anotado

    @property
    def x(self):
        return self._x or 0

    # Modificação
    # recebe 2 valores, instancia, valor
    # Para que seja possivel alterar o valor da propriedade, precisa ter o setter
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = -1


foo = Foo(10)
print(foo.x)

foo.x = 10
print(foo.x)

del foo.x
print(foo.x)
