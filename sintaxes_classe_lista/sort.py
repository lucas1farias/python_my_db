

"""
Objetivo
    - Organizar dados em lista, levando em consideração alguns critérios

Observação
    - A ordenação leva em consideração letras maiúsculas como preferência
    - Funciona somente se todos os dados de um iterável forem do mesmo tipo
    - Executada após a criação de uma lista com dados "iguais"
"""


def do_sort(container):

    mandatory_type = "<class 'list'>"
    container_type = str(type(container))

    if mandatory_type == container_type:
        container.sort()  # Uso aqui
        return container
    return 'O dado fornecido não é uma lista'


if __name__ == '__main__':
    email_msg = """
        Olá, Lucas Farias Santos,
        Sua senha de login foi alterada. Se você acha que isso seja um erro, clique no botão abaixo para acessar nosso
        portal de suporte""".split()

    list_of_values = [25, 7, 29, 91, 35, 85, 2, 90, 63, 3, 32, 71, 21, 98, 82, 52, 72, 79, 93, 38, 19, 62, 95, 67, 2.2]

    languages = ('C', 'Python', 'JS')

    print(do_sort(container=email_msg))
    print(do_sort(container=list_of_values))
    print(do_sort(container=languages))
