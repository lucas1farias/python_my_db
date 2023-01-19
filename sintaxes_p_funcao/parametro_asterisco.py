

# Função normal (parâmetros após o asterisco devem ter argumentos nomeados)
def add_to_dictionary(where, *, key, value):
    where[key] = value


if __name__ == '__main__':
    try:
        var = {}
        print([1], var)
        add_to_dictionary(var, key=0, value=0)
        print([2], var)
        add_to_dictionary(var, 1, 1)
        print([3], var)

    except TypeError as error:
        print(error)
