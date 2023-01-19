

"""
f'{person = }'         [Forma de exibir uma variável como é feito na IDE sem precisar digitar manualmente o nome da var]
"""


def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 170. Debugger mais simples com f-strings
    """


# fstring + operador walrus
print(1, f'{(nome := "Carlos")}')

# fstring + operador walrus + =
print(2, f'{(vogais := "a-e-i-o-u".split("-")) = }')
print(3, f'{"".join([x for x in "Augusto"][::-1]) = }')
print(4, f'{"".join(list(filter(lambda y: y != "v", "var"))) = }')
print(5, f"{''.join(['Errado' if len('string') == 7 else 'Errado: {}'.format(len('string'))]) = }")
print(6, f"{[round((x / 1.7) ** 1.7, 1) for x in range(7, 11)] = }")
