

from datetime import datetime, time
from typing import Literal


class Time:
    def __init__(self, clock_type: Literal[1, 2] = 1, date_type: Literal[1, 2, 3] = 1):
        self.clock_type = clock_type
        self.date_type = date_type
        self.time = ''
        self.date = ''
        self.month = ''
        self.setup = datetime.today()

        if self.clock_type == 1:
            self.time = str(time(hour=self.setup.hour, minute=self.setup.minute, second=self.setup.second))
        elif self.clock_type == 2:
            self.time = str(self.setup).split()[1][:8]

        if self.date_type == 1:
            self.date = str(self.setup).split()[0]
        elif self.date_type == 2:
            self.date = str(datetime(month=self.setup.month, day=self.setup.day, year=self.setup.year)).split()[0]
        elif self.date_type == 3:
            self.day = self.shaper(what='day')
            self.date = self.setup.strftime(f'{self.day} of %B of %Y')
        elif self.date_type == 4:
            self.month = self.shaper(what='month')
            self.date = self.setup.strftime(f'%d de {self.month} de %Y')

    def shaper(self, what: Literal['day', 'month']):
        if what == 'day':
            day = self.setup.day
            sufixes = ('1st', '2nd', '3rd')
            sufixes_int = (1, 2, 3)

            for pos, i in enumerate(sufixes_int):
                if day == i:
                    day = sufixes[i]
                    return day
                else:
                    day = f'{day}th'
                    return day
        else:
            month = str(self.setup.strftime('%B'))
            months = [*'January.February.March.April.May.June.July.August.September.October.November.December'.split('.')]
            months_br = [*'janeiro.fevereiro.março.abril.maio.junho.julho.agosto.setembro.outubro.novembro.dezembro'.split('.')]

            for pos, i in enumerate(months):
                if month == i:
                    month = months_br[pos]
                    return month


if __name__ == '__main__':
    clock_type_1 = Time()
    clock_type_2 = Time(clock_type=2)

    date_type_1 = Time(date_type=1)
    date_type_2 = Time(date_type=2)
    date_type_3 = Time(date_type=3)
    date_type_4 = Time(date_type=4)

    print(f'Relógio tipo 1: [ {clock_type_1.time} ]')
    print(f'Relógio tipo 2: [ {clock_type_2.time} ]')
    print(f'Data tipo 1: [ {date_type_1.date} ]')
    print(f'Data tipo 2: [ {date_type_2.date} ]')
    print(f'Data tipo 3: [ {date_type_3.date} ]')
    print(f'Data tipo 4: [ {date_type_4.date} ]')
