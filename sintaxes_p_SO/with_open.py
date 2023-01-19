

from os import chdir


def infos():
    """
    Objetivo:
        criar um módulo de texto com inserção de dado único, ou seja, sobreposição, caso algo novo seja escrito

    Objetivo 2:
        criar um módulo de texto com inserção de dados múltiplos, ou seja, acumulação, caso algo novo seja escrito

    Objetivo 3:
        ler dados de um módulo de texto criado previamente à leitura
    """


# Forma mais atual de criar módulo, com sobreposição de dados 'w'
def ex3() -> None:
    # A forma mais nova, cria uma variável interna, ao invés de externa
    with open('testar3.txt', 'w') as txt:
        txt.write('Bem-vindo ao Python - exemplo 3')
    with open('testar3.txt', 'w') as txt:
        txt.write('Bem-vindo ao Python - exemplo 3.1')
        # A forma mais nova dispensa o método de fechar um módulo, pois ela faz isso automaticamente


# Forma mais atual de criar módulo, com acumulação de dados 'a'
def ex4() -> None:
    with open('testar4.txt', 'a') as txt:
        txt.write('Bem-vindo ao Python - exemplo 4\n')
    with open('testar4.txt', 'a') as txt:
        txt.write('\nBem-vindo ao Python - exemplo 4.1')


# Forma mais atual de ler um módulo 'r'
def ler_ex4() -> None:
    with open('testar4.txt', 'r') as txt:
        print(ler := txt.read())


ex4(), ler_ex4()
