

print([1], 'y' in 'Python')
print([2], ('Sim' if 'i' in 'Python' else 'Não'))

if 7 in range(7, 11):
    print([3], 'ok')


def sample(value, box):
    return 'Presente' if value in box else 'Ausente'


print([4], sample(value=0, box=[1, 2, 3]))
