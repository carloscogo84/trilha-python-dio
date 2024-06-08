"""
COMANDOS DO MODO INTERATIVO
Usado para aplicações rápidas no terminal

No terminal digite python (enter)
Para sair digite exit()
para limpar contrl + l
para sair da documentação do help - aperte (q) enter

Exemplo:
10 + 10 já exibe o resultado no terminal sem o print 

Outra forma de abrir o modo interativo é digitar python -i mais o nome do arquivo

Exemplo:
python -i _1_primeiro_programa.py

FUNÇÃO DIR

Sem argumentos retorna a lista de nomes no escopo local atual
exemplo:
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
importando o módulo matemático
import math
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'math']
tudo que se declara será incluido

Com argumentos retorna uma lista de atributos validos para o objeto
dir(100)
Há muitos métodos dentro de um inteiro, float entre outros

FUNÇÃO HELP

Invoca o sistema de ajuda integrado, é possível fazer buscas em modo interativo

help()


"""