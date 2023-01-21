

from os import chdir, getlogin
from random import choice


class File:

    def __init__(self, where, amount):
        self.where = where
        self.amount = amount + 1  # Começa a contagem do 1 e por ser usada num range, precisa do + 1
        self.chars = [*'abcdefghijklmnopqrstuvwxyz123456789']
        self.formats = (
            '.txt', '.docx', '.ppt', '.xml', '.py', '.ts', '.c', '.js', '.exe', '.bat', '.dll', '.init', '.md',
            '.html', '.css'
        )
        self.prefix = 'C:/Users/'
        self.user = getlogin()
        self.path = self.prefix + self.user + '/' + self.where
        self.move_to_path()

    def move_to_path(self):
        chdir(self.path)

    def create(self):
        for qty in range(1, self.amount):
            file_name = "".join([choice(self.chars) for n in range(7)])
            file_format = choice(self.formats)
            file_ = file_name + file_format
            with open(file_, 'w') as file_obj:
                pass


if __name__ == '__main__':
    file = File(where='Desktop/dir_container', amount=choice(range(1, 26)))
    file.create()
