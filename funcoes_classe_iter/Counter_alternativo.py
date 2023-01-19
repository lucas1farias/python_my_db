

"""
Objetivo:
    mostrar duas formas de contar caracteres usando a classe dicionário

Objetivo 2:
    gerar um dicionário com dados de outras classes
"""
# todo Tutorial 10


def etapas():
    """
    1. a chave é criada antes de ter um valor [ d[string] ]
    2. o valor da chave é a própria busca do valor da chave [ d.get(string) ]
    3. só que o valor ainda não existe, pois apenas a chave foi definida, então geraria-se um KeyError
    4. mas o parâmetro 2, dá um valor à chave recem-criada [ 0 ]
    """


def char_counter(sentence: str):
    report = {}
    for letter in sentence:
        report[letter] = report.get(letter, 0) + 1
    print(report)
    return dict(sorted(report.items(), key=lambda i: i[1], reverse=True))


print(char_counter(sentence='Alceu Fernando Veras Castro'))
print(char_counter(sentence=[0, True, 'void', True, range(1), 0]))
# def contar_caracteres(texto: str) -> None:
#     """"""
#     # Forma 1
#     # box = {}
#     # for string in texto:
#     #     chave_contada = box.get(string, 0)
#     #     chave_contada += 1
#     #     box[string] = chave_contada
#     # print(box)
#
#     # Forma 2
#     box = {}
#     for string in texto:
#         box[string] = box.get(string, 0) + 1
#     print(box)
#
# def contar_caracteres2(texto: str) -> None:
#     """"""
#     from collections import Counter
#     print(dict(Counter(texto)))
#
# if __name__ == '__main__':
#     contar_caracteres('banana')
#     contar_caracteres2('banana')
