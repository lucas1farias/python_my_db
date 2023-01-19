

"""
Objetivo:
    - Converter valor inteiro para sua versão binária

Observação:
    - Os dois primeiros índices do retorno do método, não fazem parte da conversão, então eles são ignorados

Relacionamento:
    @int
"""


def integer_to_binary(value):

    this_message_error = 'Apenas números inteiros são permitidos'
    try:
        before_value = value
        value = bin(value)
        value = str(value)[2:]
        return f'Valor antes: {before_value}    Valor agora (binário): {value}'
    except ValueError:
        return this_message_error


def integer_to_binary_v2(value):

    this_message_error = 'Apenas números inteiros são permitidos'
    try:
        before_value = value
        value = format(value, 'b')
        return f'Valor antes: {before_value}    Valor agora (binário): {value}'
    except ValueError:
        return this_message_error


if __name__ == '__main__':
    print([1], integer_to_binary(value=7))
    print([2], integer_to_binary_v2(value=7))
    print([3], integer_to_binary_v2(value=''))
