

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
