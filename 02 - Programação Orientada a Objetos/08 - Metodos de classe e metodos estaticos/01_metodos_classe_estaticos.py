class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # TER ACESSO DO CONTEXTO DA CLASSE
    # criando uma fabrica
    @classmethod  # transforma em metodo de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    # NÃO PRECISO DE CONTEXTO DE CLASSE E NEM DA INSTANCIA DO OBJETO
    # Metodo estatico
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


# chamando metodo de classe
p = Pessoa.criar_de_data_nascimento(1984, 4, 4, "Carlos")
print(p.nome, p.idade)

# chamando metodo estatico
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
