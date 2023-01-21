

from datetime import datetime


def get_day_of_week():
    from datetime import datetime

    week_days = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    week_day_integer = datetime.now().isoweekday()
    for pos, i in enumerate(week_days):
        pos = pos + 1
        if week_day_integer == pos:
            if week_days[pos - 1] != 'Sábado' and week_days[pos - 1] != 'Domingo':
                return week_days[pos - 1] + '-feira'
            else:
                return week_days[pos - 1]


class Day:
    def __init__(self):
        self.days = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
        self.day_int = datetime.now().isoweekday()

    def of_week(self):
        for pos, i in enumerate(self.days):
            pos = pos + 1
            if self.day_int == pos:
                if self.days[pos - 1] != 'Sábado' and self.days[pos - 1] != 'Domingo':
                    return self.days[pos - 1] + '-feira'
                else:
                    return self.days[pos - 1]


if __name__ == '__main__':
    # ========== ESTRUTURAL ==========
    print(get_day_of_week())
    # ========== POO ==========
    day = Day()
    print(day.of_week())
