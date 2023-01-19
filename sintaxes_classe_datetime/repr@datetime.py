

from datetime import datetime


def objetivo():
    """
    Converter um objeto [ datetime ] para [ str ]
    Relacionados: ver módulo [ !r.py ]
    """


def get_date_database(datetime_var: datetime) -> tuple:
    print(repr(datetime_var))
    date_data = repr(datetime_var).replace('datetime', '').replace('(', '').replace(')', '').replace(' ', '').replace('.', '').split(',')
    date_data = tuple([int(date_cell) for date_cell in date_data])
    return date_data


print([1], hoje := datetime.now())
calendar = get_date_database(datetime_var=hoje)
print(calendar)
# print([2], repr(hoje))
#
# # O método [ repr ] converte um objeto [ datetime ] para [ str ], tornando a filtragem de dados mais fácil
# print([3], hoje_lista := repr(hoje).replace('datetime', '')
#                                    .replace('.', '')
#                                    .replace('(', '')
#                                    .replace(')', '')
#                                    .replace(' ', '')
#                                    .split(','))
