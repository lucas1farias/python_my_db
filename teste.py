

# from random import choice
#
# times = 0
# child_names = [
#     {'name': 'Ártico', 'value': 0},
#     {'name': 'Amanhecer', 'value': 0},
#     {'name': 'Próspero', 'value': 0},
#     {'name': 'Dominus', 'value': 0},
#     {'name': 'Argus', 'value': 0},
#     {'name': 'Fergus', 'value': 0},
#     {'name': 'Logan', 'value': 0}
# ]
#
# while times < 365:
#     chosen_name = choice([key['name'] for key in child_names])
#     for index, key in enumerate(child_names):
#         if chosen_name == key['name']:
#             child_names[index]['value'] += 1
#
#     board = f"""
#         Ártico    || escolhido {child_names[0]['value']} vezes
#         Amanhecer || escolhido {child_names[1]['value']} vezes
#         Próspero  || escolhido {child_names[2]['value']} vezes
#         Dominus   || escolhido {child_names[3]['value']} vezes
#         Argus     || escolhido {child_names[4]['value']} vezes
#         Fergus    || escolhido {child_names[5]['value']} vezes
#         Logan     || escolhido {child_names[6]['value']} vezes
#         """
#
#     result = {key['value']: key['name'] for key in child_names}  # Inversão das chaves
#     winner = max(result)
#     winner_name = result.get(winner)
#     times += 1
#     if times == 365:
#         print(board)
#         print(f'Vencedor: {winner_name} | {winner} escolhas |')

dict_ = {0: 1, 2: 3}
list_ = [3, 0, 2, 1]
set_ = {0, 1, 3, 2}
string_ = '0213'
tuple_ = (3, 2, 0, 1)


def where_method_is(method):
    box = []
    types = ('dicionário', 'lista', 'conjunto', 'string', 'tupla')
    iter_libraries = (dir({'': ''}), dir([]), dir(set({})), dir(''), dir(()))
    for pos, method_array in enumerate(iter_libraries):
        if method in method_array:
            box.append(types[pos])
    return f'{method} -> {box}'


methods_notation = (
    where_method_is('add'), where_method_is('append'), where_method_is('center'), where_method_is('clear'),
    where_method_is('copy'), where_method_is('count'), where_method_is('difference'), where_method_is('discard'),
    where_method_is('extend'), where_method_is('find'), where_method_is('index'), where_method_is('intersection'),
    where_method_is('items'), where_method_is('keys'), where_method_is('values'), where_method_is('update'),
    where_method_is('get'), where_method_is('insert'), where_method_is('lower'), where_method_is('max'),
    where_method_is('pop'), where_method_is('replace'), where_method_is('split')
)

# for report in methods_notation:
#     print(report)
