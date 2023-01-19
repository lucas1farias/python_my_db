

def add_multiple_data(single_data: bool, receiver, value=None, **kwargs):
    """
    ===== Objetivo ===== \n
    * Adicionar um ou vários dados em um dado do tipo conjunto \n
    * A função pode ser usado em linha, se separado por vírgula
    """

    if single_data:
        receiver.add(value)
    else:
        for data in kwargs.values():
            receiver.add(data)


if __name__ == '__main__':
    set_box = set({})
    add_multiple_data(single_data=False, receiver=set_box, kw1=(), kw2=0, kw3=None)
    print(set_box)
