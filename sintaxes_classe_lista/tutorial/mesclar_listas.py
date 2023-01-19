

"""
Soma de listas
"""

lista, lista2 = [*range(1, 4)], [*range(4, 6)]
lista3 = [None]
lista4 = [True, False, *lista3]

print([1], lista)
print([2], lista2)
print([3], lista + lista2)
print([4], lista4)
