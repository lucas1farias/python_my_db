

from datetime import datetime
from typing import Dict, Tuple


class Life:

    def __init__(self, birthday: Tuple[int, int, int]):
        self.birthday: Dict[str, int] = {'year': birthday[0], 'month': birthday[1], 'day': birthday[2]}
        self.today: datetime = datetime.now()
        self.age_full = self.my_life_days()
        self.age = str(self.age_full).split()[0]

    def my_life_days(self):
        birthday = datetime(year=self.birthday['year'], month=self.birthday['month'], day=self.birthday['day'])
        return self.today - birthday


if __name__ == '__main__':
    obj_ = Life(birthday=(1992, 7, 16))
    print(obj_.age_full)
    print(obj_.age)
