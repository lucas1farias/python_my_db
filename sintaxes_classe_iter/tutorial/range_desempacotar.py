

"""
Desempacotamento de um range
"""

var = range(4)
print([1], var)        # range normal não é exibíbel sem ser desempacotada
print([2], *var)       # range desempacotada, apenas exibe dados
print([3], list(var))  # range desempacotada com construtor, cria um tipo de dado iterável
