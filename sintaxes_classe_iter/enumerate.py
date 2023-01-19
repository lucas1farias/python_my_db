

language = 'Python'
print(tuple(enumerate(language)))

# Principal uso (opinião): Achar índices de dados procurados
for pos, i in enumerate(language):
    if i == 'y':
        print(f'A letra "y" se encontra no índice {pos}')
