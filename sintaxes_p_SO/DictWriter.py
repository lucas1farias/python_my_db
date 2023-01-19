

from os import chdir
from csv import DictWriter


def infos():
    """
    Objetivo
         Criar módulo csv (arquivo de tabela com separação dos campos por meio de vírgula)
    """


chdir("/csv")

with open('dictWrite.csv', 'w') as csv:
    fields = DictWriter(csv, fieldnames=('name', 'age', 'nationality'))

    # Valores dos atributos/campos
    names = ('Maria', 'Augusto', 'Leda', 'Ana', 'Marcos', 'Helena', 'Sandra', 'Sonya', 'Otavio', 'Lua')
    ages = (10, 14, 21, 17, 33, 40, 20, 11, 27, 15)
    nationalities = (
        'Brazilian', 'Russian', 'Egyptian', 'English', 'American', 'Canadian', 'French', 'Mexican', 'Indian', 'Chinese'
    )

    # Container
    db = []

    # Anexação dos dados em forma de objeto JSON
    for pos, name in enumerate(names):
        db.append({'name': name, 'age': ages[pos], 'nationality': nationalities[pos]})

    # Escrita dos campos no módulo .csv
    fields.writeheader()

    # Escrita de cada objeto JSON como uma linha no módulo .csv
    for obj_ in db:
        fields.writerow(obj_)
