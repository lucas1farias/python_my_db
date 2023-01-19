

"""
Objetivo:
    retornar [ True ou False ] para se um dado encontra-se dentro de uma classe iterável
    o método [ .__contains__() ] é similar a palavra reservada Python [ in ]
"""


# @dict @list @range @set @str @tuple
def scan(class_name, the_data, target_value):
    try:
        print(class_name, the_data.__contains__(target_value))
    except AttributeError as error:
        print('{}{}{}'.format('\033[1:31m', error, '\033[m'))


types = [
    'bool', 'complexo', 'dicionário', 'flutuante', 'inteiro', 'lista', 'nenhum', 'range', 'conjunto', 'string', 'tupla',
]
data = [True, 7j, {1: 2}, 7.0, 7, [-7, '...'], None, range(-7, -6), {-7}, '...', (-7,)]
values = [True, 3j, 1, 7, 7.0, ['...'], None, -7, None, '.', (-7)]

for index in range(len(types)):
    scan(class_name=types[index], the_data=data[index], target_value=values[index])

# Similaridade de [ .__contains__() ] com [ in ]
print([1], countries := ('Brasil', 'America do Sul', 'Hemisfério Norte').__contains__('Brasil'))
print([2], countries_in := 'Brasil' in ('Brasil', 'America do Sul', 'Hemisfério Norte'))
