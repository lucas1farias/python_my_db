

from random import shuffle

items = ['Água', 'Alimento', 'Medicamento', 'Munição']
amounts = [str(n) for n in range(6)]
shuffle(items)
shuffle(amounts)
amounts = ".".join(amounts)[0:7]
items = ".".join(items)

print('\n')
print(amounts.center(100))
print(items.center(100))
