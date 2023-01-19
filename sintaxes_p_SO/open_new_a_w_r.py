

from os import chdir
from typing import Literal


def file_manager(file_name: str, action: Literal['a', 'w', 'r'], *args) -> None:

    with open(file_name, action) as txt:
        if action == 'r':
            file_content = txt.read()
            print(file_content)
        else:
            for index in args:
                txt.write(index)
                txt.write('\n')


if __name__ == '__main__':
    chdir('csv')
    # file_manager('open_w_new.txt', 'w', 'Haha', 'Suave?', 'Belezinha?')
    # file_manager('open_w_new.txt', 'w', 'Hehe', 'Sussa?', 'De boa?')
    # file_manager('open_w_new.txt', 'a', 'Oi', 'Beleza?', 'Como vai as coisas?')
    # file_manager('open_w_new.txt', 'w', 'Hi', 'What is up?', 'How are you doing?')
    # file_manager('open_w_new.txt', 'r')
