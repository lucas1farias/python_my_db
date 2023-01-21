

from os import chdir, listdir, getlogin, path, remove, rmdir


class Windows:

    def __init__(self, where):
        self.where = where
        self.prefix = 'C:/Users/'
        self.user = getlogin()
        self.path = self.prefix + self.user + '/' + self.where
        self.move_to_path()
        self.path_elements = listdir()
        self.files = []
        self.dirs = []

    def move_to_path(self):
        chdir(self.path)

    def do_scan(self):
        for pos, content in enumerate(self.path_elements):
            if not path.isfile(content):
                self.dirs.append(content)
            else:
                self.files.append(content)

    def the_files(self):
        return f'{len(self.files)} arquivo(s):\n {self.files}'

    def the_dirs(self):
        return f'{len(self.dirs)} pasta(s):\n {self.dirs}'

    def reported_data(self):
        print(self.files)
        print(self.dirs)

    def remove_dirs(self):
        for directory in self.dirs:
            rmdir(directory)

    def remove_files(self):
        for file in self.files:
            remove(file)


if __name__ == '__main__':
    place = Windows(where='Desktop/dir_container')
    place.do_scan()
    print(place.the_files())
    print(place.the_dirs())
    place.remove_dirs()
    place.remove_files()
