

"""
Função que simula sum()
"""


def sum_prototype(*args):
    count = 0
    for each_number in args:
        count += each_number
    print(count)


sum_prototype(1, 7, 200)
