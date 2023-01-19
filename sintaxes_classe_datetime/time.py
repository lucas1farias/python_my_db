

"""
Objetivo:
    - Criar uma variável de tempo customizada
    - Criar uma variável de tempo com a ajuda de [datetime], sem precisar formatar
"""


def show_time_now():
    from datetime import time, datetime

    clock = datetime.today()  # variável suporte
    the_time = time(hour=clock.hour, minute=clock.minute, second=clock.second)
    return the_time


if __name__ == '__main__':
    from datetime import time
    # Exemplo com a ajuda do [ datetime ] para ter a hora em tempo real, com formatação pronta
    print(show_time_now())
    # Exemplo aparte da função
    custom_clock = time(1, 2, 3, 4)
    print([1], custom_clock)
    print([2], custom_clock.hour)
    print([3], custom_clock.minute)
    print([4], custom_clock.second)
    print([5], custom_clock.microsecond)
