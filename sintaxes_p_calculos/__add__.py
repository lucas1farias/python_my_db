

"""
Objetivo:
    - Executar subtração ou soma entre classes numéricas
"""


class Add:

    @property
    def increase(self):
        return self.__increase

    @increase.setter
    def increase(self, new):
        self.__increase = new

    @property
    def decrease(self):
        return self.__decrease

    @decrease.setter
    def decrease(self, new):
        self.__decrease = new

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new):
        self.__value = new

    def __init__(self, increase, decrease, value):
        self.__increase = increase
        self.__decrease = decrease
        self.__value = value

    def __add__(self, other_value):
        if self.__increase:
            self.__value = self.__value.__add__(other_value)
        if self.__decrease:
            self.__value = self.__value.__add__(-other_value)


if __name__ == '__main__':
    sample = Add(increase=True, decrease=False, value=7)
    print(sample.value)
    sample.__add__(other_value=3)
    print(sample.value)
    sample.increase = False
    sample.decrease = True
    sample.__add__(other_value=8)
    print(sample.value)
