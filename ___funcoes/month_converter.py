

from random import choice
from time import sleep


def mtd_month_converter_int_str(month: int):
    """"""

    # These two vars need to have the same length, otherwise the loop below will fail on picking the right choice
    months = 'january,february,march,april,may,june,july,august,september,october,november,december'.split(',')
    months_int = [*range(1, 13)]

    for i in range(len(months)):
        if month == months_int[i]:
            return months[i]


if __name__ == '__main__':
    numbers = list(range(1, 13))
    while True:
        chosen = choice(numbers)
        print([chosen, mtd_month_converter_int_str(month=chosen)])
        sleep(1)
