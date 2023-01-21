

from typing import Literal


class Month:
    def __init__(self, month_id: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], lang: Literal['br', 'us']):
        self.month_id = month_id
        self.lang = lang
        self.months = 'january,february,march,april,may,june,july,august,september,october,november,december'.split(',')
        self.months_br = 'janeiro,fevereiro,março,abril,maio,junho,julho,agosto,setembro,outubro,novembro,dezembro'.split(',')
        self.month = self.month()

    def month(self):
        for i in range(len(self.months)):
            if self.month_id - 1 == i:
                if self.lang == 'us':
                    return self.months[i]
                else:
                    return self.months_br[i]


def mtd_month_converter_int_str(month: int):
    """"""

    # These two vars need to have the same length, otherwise the loop below will fail on picking the right choice
    months = 'january,february,march,april,may,june,july,august,september,october,november,december'.split(',')
    months_int = [*range(1, 13)]

    for i in range(len(months)):
        if month == months_int[i]:
            return months[i]


if __name__ == '__main__':
    month = Month(month_id=7, lang='br')
    print(month.month)
    month = Month(month_id=7, lang='us')
    print(month.month)
