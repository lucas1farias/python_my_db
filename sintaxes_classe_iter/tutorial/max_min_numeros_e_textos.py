

"""
Curiosidade? construtores [ max() ] e [ min() ] só funcionam se seus dados forem todos os mesmos
"""

numerics = [1, 2]
numerics_str = ['1', '2']
vowels_one_upper = [*'a.e.i.o.U'.split('.')]
vowels = [*'a.e.i.o.u'.split('.')]
numerics_and_vowels = [*'a.e.i.o.u.1.2.3'.split('.')]
lista_hibrida = [*numerics, *numerics_str]

# print(max(lista_hibrida))  # TypeError: '>' not supported between instances of 'str' and 'int'
# print(min(lista_hibrida))  # TypeError: '>' not supported between instances of 'str' and 'int'

print(f'[1] Da lista {numerics}, o maior dado é: {max(numerics)}')
print(f'[2] Da lista {numerics}, o menor dado é: {min(numerics)}')

print(f'[3] Da lista {numerics_str}, o maior dado é: {max(numerics_str)}')
print(f'[4] Da lista {numerics_str}, o menor dado é: {min(numerics_str)}')

# Quando todos os caracteres não são de cacha similar, o construtor [ min ] coloca cacha alta por último
print(f'[5] Da lista {vowels_one_upper}, o maior dado é: {max(vowels_one_upper)}')
print(f'[6] Da lista {vowels_one_upper}, o menor dado é: {min(vowels_one_upper)}')

# Quando todos os caracteres são cacha baixa, a ordem segue a lógica natural
print(f'[7] Da lista {vowels}, o maior dado é: {max(vowels)}')
print(f'[8] Da lista {vowels}, o menor dado é: {min(vowels)}')

# Quando os caracteres são misturados em tipos, a precedência segue letras e números
print(f'[9] Da lista {numerics_and_vowels}, o maior dado é: {max(numerics_and_vowels)}')
print(f'[10] Da lista {numerics_and_vowels}, o menor dado é: {min(numerics_and_vowels)}')
