

"""
Objetivo:
    informar numa função, os tipos de retorno exatos que ela pode gerar, dentro de uma lista
"""

# from random import choice
from typing import Literal, Union


def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 169. Tipos de dados mais precisos
    Tempo  # 06:10
    """


def fazer_conta(v: Union[int, float], op: Literal['+', '-', '*', '/', '**', '|'], v2: Union[int, float]) -> None:
    invalid = '\n========== Erro ==========\nO operador fornecido é inválido:'
    invalid_ = '\n========== Erro ==========\nDivisão por zero é inválida'
    try:
        if op == '+' or op == '-' or op == '*' or op == '/' or op == '**':
            conditions = [
                [f'{v} + {v2} = {v + v2:.2f}' if op == '+' else None],
                [f'{v} - {v2} = {v - v2:.2f}' if op == '-' else None],
                [f'{v} x {v2} = {v * v2:.2f}' if op == '*' else None],
                [f'{v} / {v2} = {v / v2:.2f}' if op == '/' else None],
                [f'{v} ** {v2} = {v ** v2:.2f}' if op == '**' else None],
            ]
            while [None] in conditions:
                conditions.pop(conditions.index([None]))
            print("".join(conditions[0]))

        elif op == '|':
            conditions = [[f'raiz de {v} = {v ** 0.5:.2f}' if op == '|' else None]]
            print("".join(conditions[0]))

        else:
            print(f'{invalid} {op!r}')

    except ZeroDivisionError:
        print(invalid_)


fazer_conta(13, '*', 13.1)
