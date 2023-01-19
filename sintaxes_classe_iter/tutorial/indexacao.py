

"""
========== INDEXAÇÃO ==========
    iter[::-1]                     [Inverter a ordem dos índices de qualquer iterável]
    iter[-1]                       [Acesso ao último índice]
    iter[int]                      [Acesso a um índice]
    iter[int:]                     [Acesso a todos os índices, começando do especificado no "int" 1]
    iter[int:int]                  [Acesso a todos os índices dentro do range definido entres os 2 "int"]
    iter[int:int:int]              [Acesso de todos os índices dentro do range especificado entres os 2 "int", com saltos definido no "int" 3]
    iter[int::int]                 [Acesso a partir do índice definido no "int" 1 até o final, com saltos definidos pelo "int" 2]
    iter[:int:int]                 [Acesso do índice 0 até o índice definido no "int" 1, com saltos definidos pelo "int" 2]
"""


# Indexação negativa
print(tuple(range(5, 0, -1)))   # sintaxe decrescente (comum)
print(tuple(range(7, -8, -2)))  # sintaxe decrescente com saltos (indexação negativa)
print(tuple(range(-7, 8)))      # sintaxe decrescente sem saltos (indexação negativa)
