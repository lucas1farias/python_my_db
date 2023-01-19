

word = 'Python'
print(word, end='.' + '\n')

# Imprime índices em linha com um separador entre eles
word_as_list = [letter for letter in word]
for i in word_as_list:
    print(i, end='.')
