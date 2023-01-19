

def get_day_of_week():
    from datetime import datetime

    week_days = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    week_day_integer = datetime.now().isoweekday()
    for pos, i in enumerate(week_days):
        pos = pos + 1
        if week_day_integer == pos:
            return week_days[pos - 1]


print(get_day_of_week())
