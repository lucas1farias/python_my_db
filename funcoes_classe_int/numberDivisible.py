

class Number:
    def __init__(self, single: bool = True, number: int = 1, target: int = 1, targets: tuple = ()):
        self.single = single
        self.number = number
        self.target = target
        self.targets = targets
        self.box_calculus = []
        self.msg = {
            'report': f'\n========== RELATÓRIO: NÚMEROS DIVISÍVEIS POR {self.number} ==========',
            'none_is_divisible': '========== RELATÓRIO ==========\nNenhum dos dados escolhidos é divisível por {}'
        }

    def is_divisible(self):
        if self.single:
            yes = 'é divisível'
            no = 'não é divisível'
            return f'{self.number} {yes if self.number % self.target == 0 else no} por {self.target}'
        else:
            for numb in self.targets:
                if self.number % numb == 0:
                    self.box_calculus.append((f'divisor: {numb}', f'resultado: {int(self.number / numb)}'))

            if len(self.box_calculus) != 0:
                print(self.msg['report'])
                return self.box_calculus
            else:
                print(self.msg['none_is_divisible'].format(self.number))
                return self.box_calculus


if __name__ == '__main__':
    sample_1st = Number(number=2892458, target=2)
    sample_2nd = Number(number=2892458, target=3)
    sample_3rd = Number(number=2892458, single=False, targets=tuple(range(1, 10_001)))
    sample_4th = Number(number=2892458, single=False, targets=(13, 140, 211, 270, 308, 444, 510, 612, 730, 815))

    print(sample_1st.is_divisible())
    print(sample_2nd.is_divisible())
    print(sample_3rd.is_divisible())
    print(sample_4th.is_divisible())
