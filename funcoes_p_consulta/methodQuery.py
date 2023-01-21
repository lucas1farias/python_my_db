

class Iterable:
    def __init__(self, method):
        self.method = method
        self.iterables = ('dicionário', 'lista', 'conjunto', 'string', 'tupla')
        self.iter_libraries = {
            'dict': dir({'': ''}), 'list': dir([]), 'set': dir(set({})), 'str': dir(''), 'tuple': dir(())
        }
        self.non_iterables = ('inteiro', 'flutuante', 'complexo', 'booleano', 'none')
        self.non_iter_libraries = {
            'int': dir(0), 'float': dir(1.0), 'complex': dir(0j), 'bool': dir(True), 'none': dir(None)
        }
        self.where = []

    def is_from(self):
        for pos, method_array in enumerate(self.iter_libraries.values()):
            if self.method in method_array:
                self.where.append(self.iterables[pos])

        if len(self.where) == 0:
            for pos, method_array in enumerate(self.non_iter_libraries.values()):
                if self.method in method_array:
                    self.where.append(self.non_iterables[pos])

        return f'{self.method} -> {self.where}'


if __name__ == '__main__':
    methods = (
        Iterable('add'), Iterable('append'), Iterable('center'), Iterable('clear'), Iterable('copy'), Iterable('count'),
        Iterable('difference'), Iterable('discard'), Iterable('extend'), Iterable('find'), Iterable('index'),
        Iterable('intersection'), Iterable('items'), Iterable('keys'), Iterable('values'), Iterable('update'),
        Iterable('get'), Iterable('insert'), Iterable('lower'), Iterable('pop'), Iterable('replace'), Iterable('split'),
        Iterable('conjugate'), Iterable('__trunc__'), Iterable('__repr__')
    )

    for report in methods:
        print(report.is_from())
