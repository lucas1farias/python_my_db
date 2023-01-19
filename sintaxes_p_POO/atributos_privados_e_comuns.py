

"""
===== Atrib. privado ===== \n
* Sintaxe "__.nome_atrib."
* Precisa de uma função com construtor "property" \n
* Não consegue ser chamado somente por notação ponto \n

===== Atrib. comum ===== \n
* Chamado via notação ponto
"""


class AnimalLimited:
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, new):
        self.__label = new

    def __init__(self, label):
        self.__label = label


class Animal:
    def __init__(self, label):
        self.label = label


# O atributo é privado, portanto sua chamada se dá pelo método de classe com decorador "@property"
sample = AnimalLimited(label='dog')
print([1], 'Chamado por função property:', sample.label)
sample.label = 'DOG'
print([2], 'Chamado por função property:', sample.label)

# O atributo não é privado
sample_ = Animal(label='cat')
print([3], 'Chamado por notação ponto:', sample_.label)
