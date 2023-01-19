

sample = list(range(1, 11))
print('map\n', list(map(lambda divisible_by_4: not divisible_by_4 % 4, sample)))        # transforma dados
print('filter\n', list(filter(lambda divisible_by_4: not divisible_by_4 % 4, sample)))  # filtra dados
