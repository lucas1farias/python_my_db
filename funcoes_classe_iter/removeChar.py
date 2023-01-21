

from typing import Literal


def remove_char(from_: iter, this_char: str, type_: Literal['string', 'list', 'tuple']) -> str:
    if type_ == 'string':
        return ''.join(from_.split(this_char))
    elif type_ == 'tuple' or type_ == 'list':
        return ' '.join(' '.join(from_).split(this_char))


if __name__ == '__main__':
    sentence_list = remove_char(from_=['Python', 'looks', 'cool'], this_char='o', type_='list')
    sentence_string = remove_char(from_='Python looks cool', this_char='o', type_='string')
    sentence_tuple = remove_char(from_=('Python', 'looks', 'cool'), this_char='o', type_='tuple')
    print(sentence_list)
    print(sentence_string)
    print(sentence_tuple)
