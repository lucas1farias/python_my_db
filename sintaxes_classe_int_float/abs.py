

def _abs(value) -> dict:
    """
    ===== Objetivo ===== \n
    * Converter classes numéricas [int, float, complex] de valor negativo p/ positivo
    """

    return {
        'before': f'{value = }',
        'after': f'{abs(value) = }',
        'oop_version': f'{value.__abs__() = }'
    }


class Abs:
    def __init__(self, number):
        self.number = number

    def __abs__(self):
        return f'{self.number.__abs__() = }'


if __name__ == '__main__':
    sample = _abs(value=-1)
    print('===== Versão normal =====')
    print(sample['before'])
    print(sample['after'])
    print(sample['oop_version'])

    sample_oop = Abs(number=-1.7)
    print('===== Versão oop =====')
    print(f'{sample_oop.number = }')
    print(sample_oop.__abs__())
