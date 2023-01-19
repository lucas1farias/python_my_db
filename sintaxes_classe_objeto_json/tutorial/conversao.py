

name = ('Ana', 'Ena', 'Ina')
ages = (30, 22, 19)
nationality = ('American', 'Arabian', 'Russian')
json = []
for pos, i in enumerate(name):
    json.append({'name': i, 'age': ages[pos], 'nationality': nationality[pos]})
print(json)
