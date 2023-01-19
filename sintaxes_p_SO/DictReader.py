

from csv import DictReader
from os import chdir, getcwd


def infos():
    """
    Objetivos
         Ler módulos csv já criados/existentes

    Observações
        1. O módulo csv não deve conter erros de digitação, e o formato deve ser explicitado
        2. O segundo argumento deve ser 'r', pois é a leitura de um módulo que já existe
    """


chdir("/csv")

with open('dictRead.csv', 'r') as csv:
    for each_data in DictReader(csv):
        print(each_data)

with open('dictRead.csv', 'r') as csv:
    file_content = DictReader(csv)
    for word in file_content:
        print(word['name'], word['age'], word['nationality'])
