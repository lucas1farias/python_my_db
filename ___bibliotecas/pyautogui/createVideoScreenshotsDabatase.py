

from pyautogui import screenshot
from keyboard import is_pressed
from os import chdir


class Video:

    def __init__(self, standard_img_name, storage_path):
        # self.file: str = file
        self.standard_img_name = standard_img_name
        self.storage_path = storage_path
        chdir(self.storage_path)
        self.get_each_frame()

    # def prototype(self):
    #     return stat(self.file)

    def get_each_frame(self):
        counter = 0
        while True:
            screenshot(f'{self.standard_img_name}_{counter}.png', region=(506, 40, 347, 608))
            counter += 1
            if is_pressed('q'):
                exit(0)


if __name__ == '__main__':
    try:
        obj_ = Video(standard_img_name='pht', storage_path='C:\\Users\\lucasf\\Desktop\\captures')
    except KeyboardInterrupt:
        print('\nAlgoritmo interrompido\n')
