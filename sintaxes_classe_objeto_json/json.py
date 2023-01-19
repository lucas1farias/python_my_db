

# JSON: São dados em lista com índices dicionário contendo todos as mesmas chaves, mudando somente os valores
type_list_json = [
    {'name': 'Bicicleta Specialized', 'price': 2612.20, 'fragile': False},
    {'name': 'Garrafa', 'price': 41.60, 'fragile': True},
    {'name': 'Luva', 'price': 56.80, 'fragile': False}
]

# JSON é o tipo de objeto que funciona muito bem com as funções: map, filter
expensive_ones = tuple(filter(lambda json_: json_['price'] > 200, type_list_json))
print(expensive_ones)
expensive_ones_names = (product['name'] for product in expensive_ones)
print(tuple(expensive_ones_names))
