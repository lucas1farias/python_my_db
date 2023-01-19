

def char_set(length):
    from random import choice

    data_source = 'abcdefghijklmnopqrstuvwxyz123456789'
    # print([1], tuple({}.fromkeys('abcdefghijklmnopqrstuvwxyz123456789', None)))
    code = []
    for i in range(length):
        code.extend(choice(data_source))
    print(f'Código gerado: {code}')
    return ''.join(code)


if __name__ == '__main__':
    print(char_set(length=20))
