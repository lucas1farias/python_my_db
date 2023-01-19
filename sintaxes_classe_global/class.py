

"""
Objetivo:
    mostrar a classe de um dado, seja declarado ou literal

Observação:
    1. com a classe None, não há referência, mas funciona
"""

# @global


def scan(class_name, the_data):
    try:
        print(class_name, the_data.__class__)
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))


all_types = [True, -7j, {-7: -7}, -7.0, -7, [-7], None, range(-7, -6), {-7}, '-7', (-7,)]
all_types_names = [
    'booleano', 'complexo', 'dicionário', 'flutuante', 'inteiro', 'lista', 'nenhum', 'range', 'conjunto', 'string',
    'tupla',
]

for index in range(len(all_types)):
    scan(class_name=all_types_names[index], the_data=all_types[index])
