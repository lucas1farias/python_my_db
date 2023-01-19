

json = [
    {'name': 'João', 'age': 27},
    {'name': 'Eno', 'age': 34},
    {'name': 'Rasputin', 'age': 39},
    {'name': 'Marcos', 'age': 71}
]

print('Pessoa + velha? ', max(json, key=lambda cada_valor: cada_valor['age']))
print('Pessoa + jovem? ', min(json, key=lambda cada_dado: cada_dado['age']))
print('Pessoa com maior nome? ', max(json, key=lambda cada_valor: cada_valor['name']))
print('Pessoa com menor nome? ', min(json, key=lambda cada_valor: cada_valor['name']))

playlist_json = [
    {'name': 'Chop Suey', 'played': 27},
    {'name': 'Spiders', 'played': 14},
    {'name': 'Toxicity', 'played': 39},
    {'name': 'Vermilion pt2', 'played': 71}
]

most_played = max(playlist_json, key=lambda soundtrack: soundtrack['played'])['name']
print('Música + tocada? ', most_played)
