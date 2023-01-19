

"""
Objetivo:
    esvaziar dados de classes iteráveis específicas
"""


# @dict @list @set
def scan(class_name, the_data):
    try:
        var = the_data
        var.clear()
        print(class_name, var)
    except AttributeError as error2:
        print('{}{}{}'.format('\033[1:31m', error2, '\033[m'))


all_types = [True, -7j, {-7: -7}, -7.0, -7, [-7], None, range(-7, -6), {-7}, '-7', (-7,)]
all_types_names = [
    'booleano', 'complexo', 'dicionário', 'flutuante', 'inteiro', 'lista', 'nenhum', 'range', 'conjunto', 'string',
    'tupla',
]

for index in range(len(all_types)):
    scan(class_name=all_types_names[index], the_data=all_types[index])
