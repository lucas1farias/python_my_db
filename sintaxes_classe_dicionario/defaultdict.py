

"""
Objetivo:
    nesse contexto específico, criar várias chaves com um único valor, através de uma chave = função lambda

Observação:
    1. através da palavra reservada lambda, cria-se um valor padrão para qualquer chave nova criada
    2. chaves são criadas pelos contextos: declaração e print
"""

from collections import defaultdict

people = ('Ana', 'Ena', 'Ina', 'Ona', 'Una')
sample = defaultdict(lambda: 0)
print(sample)
for i in range(len(people)):
    sample[people[i]]
print(sample)
