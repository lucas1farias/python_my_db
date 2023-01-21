

"""
Objetivo:
    Resgatar o nome de usuário sem precisar digitar
"""

from os import getlogin

print(my_user := getlogin())
