

from os import chdir


def file_manager(file_name: str, action: str, *args) -> None:

    file_repr = None

    if action == 'write_replaceable':
        file_repr = open(file_name, 'w')

    if action == 'write_appending':
        file_repr = open(file_name, 'a')

    if action == 'read':
        file_repr = open(file_name, 'r')
        file_content = file_repr.read()
        print(file_content)
        file_repr.close()
    else:
        for txt in args:
            file_repr.write(txt)
            file_repr.write('\n')
        file_repr.close()


if __name__ == '__main__':
    chdir('csv')
    # file_manager('open_w_old.txt', 'write_replaceable', 'Haha', 'Suave?', 'Belezinha?')
    # file_manager('open_w_old.txt', 'write_replaceable', 'Hehe', 'Sussa?', 'De boa?')
    # file_manager('open_w_old.txt', 'write_appending', 'Oi', 'Beleza?', 'Como vai as coisas?')
    # file_manager('open_w_old.txt', 'write_appending', 'Hi', 'What is up?', 'How are you doing?')
    # file_manager('open_w_old.txt', 'read')
