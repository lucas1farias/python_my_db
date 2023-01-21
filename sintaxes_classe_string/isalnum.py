

"""
Objetivo
    Informa se um caracter é texto ou não
    Se combinado com list comprehension e join, pode filtrar dados não textuais indesejados
"""

sentence = 'palavra!@#$%'
print("".join([char for char in sentence if char.isalnum()]))
