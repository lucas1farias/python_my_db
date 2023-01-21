

from time import sleep
from typing import Literal

sem_arg = '\033[0:30mtexto normal'
arg1 = '\033[1:30mtexto em negrito'
arg4 = '\033[4:30mtexto sublinhado'
arg7 = '\033[7:30mtexto com plano de fundo'

# print(sem_arg, '\n', arg1, '\n', arg4, '\n', arg7)
# print(arg7)


class Text:
    def __init__(self, text: str):
        self.text = text
        self.inks = tuple([str(n) for n in range(30, 38)])
        self.prefix = '\033[0:'
        self.sufix = '\033[m'
        self.prefix_bold = '\033[1:'
        self.prefix_underline = '\033[4:'
        self.prefix_filled = '\033[7:'

        # Como a sintaxe funciona (prefixos: 0, 1, 4, 7) (sufixos: 30 ao 37)
        self.ink_sample = '\033[1:30m' + text + '\033[m'

    def show_text_inked_normal(self):
        for i in self.inks:
            print(self.prefix + i + 'm' + self.text + self.sufix)
            sleep(.25)

    def show_text_inked_bold(self):
        for i in self.inks:
            print(self.prefix_bold + i + 'm' + self.text + self.sufix)
            sleep(.25)

    def show_text_inked_underlined(self):
        for i in self.inks:
            print(self.prefix_underline + i + 'm' + self.text + self.sufix)
            sleep(.25)

    def show_text_inked_filled(self):
        for i in self.inks:
            print(self.prefix_filled + i + 'm' + self.text + self.sufix)
            sleep(.25)

    def show(self, category: Literal['common', 'bold', 'underlined', 'filled']) -> None:
        if category == 'common':
            self.show_text_inked_normal()
        elif category == 'bold':
            self.show_text_inked_bold()
        elif category == 'underlined':
            self.show_text_inked_underlined()
        elif category == 'filled':
            self.show_text_inked_filled()


sample = Text(text='Python')
sample.show(category='common')
print('\n')
sample.show(category='bold')
print('\n')
sample.show(category='underlined')
print('\n')
sample.show(category='filled')
