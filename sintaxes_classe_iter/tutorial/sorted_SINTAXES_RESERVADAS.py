

"""
========== SINTAXES RESERVADAS ==========
    key=        [Método: sorted] [Passa algum atrib. que seja critério p/ organizados os índices]
    lambda:     [Método que cria uma var. que representa cada índice, p/ organizar baseado em algum critério]
    reverse=    [Método: sorted] [Inverter a ordem da organização p/ crescente (sendo o padrão decrescente)]
"""


# Esse método não requer casting, só aplicando caso queira modificar os dados
professions = ("Oftalmologista", "Professor", "Dentista", "Arquiteto", "Legista", "Advogado", "Frentista", "Prefeito")
print(tuple(sorted(professions, key=lambda var: 'ista' in var, reverse=True)))
print(tuple(sorted(professions, key=len, reverse=True)))

# Os métodos "sorted" e "filter" podem ser parecidos
print(tuple(filter(lambda i: 'ista' in i, professions)))
