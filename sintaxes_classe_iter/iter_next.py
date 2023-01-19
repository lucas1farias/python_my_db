

def objetivo():
    """
    Percorrer dados, similarmente ao loop for, só que não sendo automático (obsoleto)
    - Pode ser útil para filtrar dados pequenos
    - Para poder usar [ next() ] o dado precisa ser iterável e receber [ iter() ]
    """


nome = 'Lucas'
nome = iter(nome)

# "next()" só funciona com dados convertidos por "iter()", fora do "print()" o dado é saltado
print(next(nome))
next(nome)  # Dados chamados sem [ print() ] ficam omitidos
print(next(nome))
next(nome)
print(next(nome))


def use_method_iter(iterable):
    var = iter(iterable)
    while True:
        try:
            print(next(var), end=' ')  # v a i   t o m a r   n o   c o o l
        except StopIteration:
            break


use_method_iter('vai tomar no cool')
print('\n')

use_method_iter([0, 1, 2, 3, True])
print('\n')
