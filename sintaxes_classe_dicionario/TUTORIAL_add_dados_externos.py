

# Adicionando múltiplos dados num dicionário vazio
counters = {}

# Respectivamente: chave, chave aninhada, chave aninhada (todos devem ter mesmo tamanho)
words = ['one', 'two', 'three']
letters = ['a', 'b', 'c']
integers = [1, 2, 3]

# O loop pode usar qualquer uma das vars acima (todas têm o mesmo tamanho)
for index, value in enumerate(words):
    counters[words[index]] = {'letter': letters[index], 'number': integers[index]}

print(counters)
