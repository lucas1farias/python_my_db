

from datetime import datetime
from time import sleep
from random import choice


while True:
    this_time = datetime.now()
    delay = tuple(range(2, 6))
    sleep(choice(delay))
    
    if this_time.second in range(1, 21):
        print('Segundo está entre 1 a 20')
    elif this_time.second in range(20, 41):
        print('Segundo está entre 20 e 40')
    else:
        print('Segundo está entre 40 a 59')
