

"""
Converter inteiros em lista para string com valores pontuados
"""


def number_to_string(value: int) -> str:
    value_str = str(value)
    value_array = [i for i in value_str]

    if len(value_array) == 4:
        value_array.insert(1, '.')
    elif len(value_array) == 5:
        value_array.insert(2, '.')
    elif len(value_array) == 6:
        value_array.insert(3, '.')
    elif len(value_array) == 7:
        value_array.insert(1, '.')
        value_array.insert(5, '.')
    elif len(value_array) == 8:
        value_array.insert(2, '.')
        value_array.insert(6, '.')

    value_shaped = "".join([str(i) for i in value_array])
    return value_shaped


if __name__ == '__main__':
    value_4_digits = number_to_string(2892)
    print(value_4_digits)
    value_5_digits = number_to_string(28924)
    print(value_5_digits)
    value_6_digits = number_to_string(289245)
    print(value_6_digits)
    value_7_digits = number_to_string(2892458)
    print(value_7_digits)
    value_8_digits = number_to_string(28924580)
    print(value_8_digits)
