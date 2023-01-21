

from os import chdir, mkdir, getlogin
from random import choice


class Folder:

    def __init__(self, where, amount):
        self.where = where
        self.amount = amount + 1  # Começa a contagem do 1 e por ser usada num range, precisa do + 1
        self.chars = [*'abcdefghijklmnopqrstuvwxyz123456789']
        self.prefix = 'C:/Users/'
        self.user = getlogin()
        self.path = self.prefix + self.user + '/' + self.where
        self.move_to_path()

    def move_to_path(self):
        chdir(self.path)

    def create(self):
        for qty in range(1, self.amount):
            dir_name = "".join([choice(self.chars) for n in range(7)])
            mkdir(dir_name)


if __name__ == '__main__':
    folder = Folder(where='Desktop/dir_container', amount=choice(range(1, 26)))
    folder.create()
