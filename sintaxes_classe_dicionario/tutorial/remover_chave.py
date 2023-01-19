

if __name__ == '__main__':

    print([1], dicionario := {'x': 1, 'y': 2, 'z': 3})

    # Método 1
    dicionario.pop('x')
    print([2], dicionario)

    # Método 2
    del dicionario['y']
    print([3], dicionario)
