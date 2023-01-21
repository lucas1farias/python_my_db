

def file_rename(where, fixed_syntax, the_format, integer, random_, single=True, is_file=True, filename='old', new_name='new'):
    """
    :param is_file:                 avoid folder and file with same names to be edited at once
    :param new_name:                self explanatory
    :param single:                  when there is only one target file/folder
    :param filename:                self explanatory
    :param where:                   the path where the files are stored
    :param fixed_syntax:            fixed name for all files (pattern)
    :param the_format:              fixed file format for all the files
    :param integer:                 the number placed in each file name, increasing 1 by 1, at the end
    :param random_:                 in case the syntax stored in the name of the files is not progressive numbers
    """

    from os import listdir, rename, path
    from uuid import uuid4

    before = '========== ANTES =========='
    after = '========== DEPOIS =========='
    main_folder = listdir(where)

    # Mostrar como estão os arquivos na pasta atual antes da função executar seus procedimentos
    # print(before)
    # for data in main_folder:
    #     print(data, end='    ')
    # print('\n')

    # Apenas um arquivo/pasta e com nome escolhido
    if single and random_ is False:
        # TODO: "and" é uma necessidade de evitar que um local tenha pasta e arquivo de mesmo nome editadas juntas
        # TODO: Se for arquivo, só o seu nome é editado, e a pasta de mesmo nome não mudará (vice-versa)
        # É arquivo
        if path.isfile(f'{where}\\{filename}{the_format}') and is_file:
            # TODO: rename(2 pars) -> rename(path\\nome do arquivo, path\\novo nome.formato)
            rename(where + '\\' + filename + the_format, where + '\\' + new_name + the_format)
        # É pasta
        if path.isdir(f'{where}\\{filename}') and not is_file:
            rename(where + '\\' + filename, where + '\\' + new_name)

    # Apenas um arquivo/pasta e com nome uuid4
    if single and random_ is True:
        if path.isfile(f'{where}\\{filename}{the_format}') and is_file:
            # TODO: rename(2 pars) -> rename(path\\nome do arquivo, path\\novo nome.formato)
            rename(where + '\\' + filename + the_format, where + '\\' + f'{uuid4()}' + the_format)
        # É pasta
        if path.isdir(f'{where}\\{filename}') and not is_file:
            rename(where + '\\' + filename, where + '\\' + f'{uuid4()}')

    # Múltiplos arquivos/pastas
    else:
        # Nome customizado p/ todos (nome customizado + nome atual) (indicar pertencimento a um grupo)
        if random_ is False:
            for content in main_folder:
                # É arquivo
                if path.isfile(f'{where}\\{content}'):
                    # Separar nome da extensão do arquivo
                    before_extension = content.split('.')[0]
                    extension = content.split('.')[1]
                    print(where + '\\' + content, where + '\\' + fixed_syntax + before_extension + '.' + extension)
                    rename(where + '\\' + content, where + '\\' + fixed_syntax + before_extension + '.' + extension)
                # É pasta
                if path.isdir(f'{where}\\{content}'):
                    rename(where + '\\' + content, where + '\\' + fixed_syntax + content)

        # Nome uuid4
        if random_ is True:
            for content in main_folder:
                if path.isfile(f'{where}\\{content}'):
                    extension = content.split('.')[1]
                    rename(where + '\\' + content, where + '\\' + fixed_syntax + f'{uuid4()}' + '.' + extension)
                if path.isdir(f'{where}\\{content}'):
                    rename(where + '\\' + content, where + '\\' + fixed_syntax + f'{uuid4()}')

        # Nome numérico (ex: arquivo1, arquivo2)
        if random_ == 'int':
            for content in main_folder:
                if path.isfile(f'{where}\\{content}'):
                    rename(where + '\\' + content, where + '\\' + f'{integer}' + the_format)
                    integer += 1

    # Reatribuição dos arquivos após os procedimentos da função
    # main_folder = listdir(where)
    # print(after)
    # for data in main_folder:
    #     print(data, end='    ')


if __name__ == '__main__':

    "Arquivo único com nome uuid4"      # random_=True  new_name=''
    "Arquivo único com nome escolhido"  # random_=False  new_name='algo'
    # file_rename(where='C:\\Users\\lucasf\\Desktop\\x',
    #             fixed_syntax='',
    #             the_format='.rar',
    #             integer=None,
    #             random_=False,
    #             single=True,
    #             is_file=False,
    #             filename='3b536113-6789-4f65-9559-ac80310bdcbb',
    #             new_name='a')

    "Arquivos múltiplos com sintaxe fixa"  # random_=False
    "Arquivos múltiplos com nome uuid4"    # random_=True
    file_rename(where='c:/users/lucasf/desktop/_',
                fixed_syntax='pt3-',
                the_format='',
                integer=None,
                random_=False,
                single=False)
