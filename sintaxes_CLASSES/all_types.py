

from os import scandir
from itertools import zip_longest


class Animal:
    def __init__(self, name):
        self.name = name


type_boolean = True
type_complex = -7j
type_dict = {None: None}
type_float, type_float_n = 7.0, -7.0
type_integer, type_integer_n = 7, -7
type_list = []
type_none = None
type_range, type_range_p, type_range_n = range(4), range(1, 6), range(-7, -6)
type_set = set({})
type_string = ''
type_tuple = ()

# Tipos que requer casting .__dict__
type_object = Animal(name='snake')  # <__main__.Animal object at 0x0000016097972C20>

# Tipos que requer "casting"
type_enumerate = enumerate((1, 2, 3))                 # <enumerate object at 0x0000023838F40DC0>
type_filter = filter(lambda i: not i % 1, [1, 2, 3])  # <filter object at 0x000001A9FE2539A0>
type_generator = (i for i in (1, 2, 3))               # <generator object <genexpr> at 0x0000017653F851C0>
type_iter = iter((1, 2, 3))                           # <tuple_iterator object at 0x0000025BC4517B80>
type_map = map(lambda i: i / 2, [1, 2, 3])            # <map object at 0x00000198947D2C20>
type_scandir = scandir('C:/Users/lucasf/Desktop')     # <nt.ScandirIterator object at 0x000001B08065B7E0>
type_zip = zip({1, 2, 3}, ('Ana', 'Ena', 'Ina'))      # <zip object at 0x000001329AC61F80>
type_zip_longest = zip_longest([0], 'string')         # <itertools.zip_longest object at 0x000001C91842D1C0>

# JSON: São dados mais fáceis de fazer consulta, filtragem
type_list_json = [
    {'name': 'Bicicleta Specialized', 'price': 2612.20, 'fragile': False},
    {'name': 'Garrafa', 'price': 41.60, 'fragile': True},
    {'name': 'Luva', 'price': 56.80, 'fragile': False}
]

expensive_ones = tuple(filter(lambda json: json['price'] > 200, type_list_json))
print(expensive_ones)
expensive_ones_names = (product['name'] for product in expensive_ones)
print(tuple(expensive_ones_names))
