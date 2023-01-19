

"""
Objetivo:
    clonar dados de um iterável para outro, sem gerar um elo entre os dados envolvidos
"""


"@dict @list @set"

# Exemplo de que não há vínculo
one_set = {1}
one_set_clone = one_set.copy()
one_set.add(2)
print(one_set, one_set_clone, f"São iguais? {'Sim' if one_set == one_set_clone else 'Não'}")

# Exemplo de que há vínculo
one_list = [1]
one_list_clone = one_list
one_list.append(2)
print(one_list, one_list_clone, f"São iguais? {'Sim' if one_list == one_list_clone else 'Não'}")
