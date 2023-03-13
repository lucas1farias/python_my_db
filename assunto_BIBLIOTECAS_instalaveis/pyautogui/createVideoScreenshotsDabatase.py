

from pyautogui import screenshot, pixel, locateOnScreen
# from keyboard import is_pressed
from os import chdir
from time import sleep  # Ativar p/ casos especiais


class Video:

    def __init__(self, standard_img_name, storage_path, slow_down: bool = False, slow_in_sec: float = 0, interval: bool = False):
        # self.file: str = file
        self.slow_down = slow_down
        self.slow_in_sec = slow_in_sec
        self.interval = interval
        self.standard_img_name = standard_img_name
        self.storage_path = storage_path
        chdir(self.storage_path)
        self.get_each_frame()

    def get_each_frame(self):
        counter = 0

        if not self.interval:
            while True:
                screenshot(f'{self.standard_img_name}_{counter}.png', region=(35, 70, 1319, 655))
                counter += 1
                print(f'========== FOTOS TIRADAS ATÉ O MOMENTO ========== [{counter}]')
                if self.slow_down:
                    sleep(self.slow_in_sec)

                # if is_pressed('q'):
                #     exit(0)
        else:
            white = (255, 255, 255)
            y = 600
            sleep(7)
            while True:

                report = []
                box = [
                    pixel(530, y), pixel(540, y), pixel(550, y), pixel(560, y), pixel(570, y), pixel(580, y), pixel(590, y),
                    pixel(600, y), pixel(610, y), pixel(620, y), pixel(630, y), pixel(640, y), pixel(650, y), pixel(660, y),
                    pixel(670, y), pixel(680, y), pixel(690, y), pixel(700, y), pixel(710, y), pixel(720, y), pixel(730, y),
                    pixel(740, y), pixel(750, y), pixel(760, y), pixel(770, y), pixel(780, y), pixel(790, y), pixel(800, y),
                ]
                for pos, coord in enumerate(box):
                    if coord == white:
                        screenshot(f'{self.standard_img_name}_{counter}.png', region=(35, 70, 1319, 655))
                report.clear()


if __name__ == '__main__':
    try:
        obj_ = Video(
            standard_img_name='pht',
            storage_path='C:\\Users\\lucasf\\Desktop\\dir_container',
            slow_down=True,
            slow_in_sec=.7,
            interval=False
        )
    except KeyboardInterrupt:
        print('\nAlgoritmo interrompido\n')
