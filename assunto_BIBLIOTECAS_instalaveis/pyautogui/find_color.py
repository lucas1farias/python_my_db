

from pyautogui import pixel, hotkey, moveTo, click
from time import sleep


# while True:
#     white = (255, 255, 255)
#
#     y = 625
#     report = []
#     box = [
#         pixel(530, y), pixel(540, y), pixel(550, y), pixel(560, y), pixel(570, y), pixel(580, y), pixel(590, y),
#         pixel(600, y), pixel(610, y), pixel(620, y), pixel(630, y), pixel(640, y), pixel(650, y), pixel(660, y),
#         pixel(670, y), pixel(680, y), pixel(690, y), pixel(700, y), pixel(710, y), pixel(720, y), pixel(730, y),
#         pixel(740, y), pixel(750, y), pixel(760, y), pixel(770, y), pixel(780, y), pixel(790, y), pixel(800, y),
#     ]
#     for pos, coord in enumerate(box):
#         if coord == white:
#             report.append((pos, True))
#         else:
#             report.append((pos, False))
#     # print(report)
#     for tuple_ in report:
#         if True in tuple_:
#             print(f'Imagem possui legenda')
#             hotkey('right')
#             break
#         else:
#             print(f'Imagem NÃO possui legenda')
#             hotkey('right')
#             break
#     report.clear()

while True:
    white = (255, 255, 255)
    y = 625
    editor_del_icon = (576, 617)
    report = []
    box = [
        pixel(530, y), pixel(540, y), pixel(550, y), pixel(560, y), pixel(570, y), pixel(580, y), pixel(590, y),
        pixel(600, y), pixel(610, y), pixel(620, y), pixel(630, y), pixel(640, y), pixel(650, y), pixel(660, y),
        pixel(670, y), pixel(680, y), pixel(690, y), pixel(700, y), pixel(710, y), pixel(720, y), pixel(730, y),
        pixel(740, y), pixel(750, y), pixel(760, y), pixel(770, y), pixel(780, y), pixel(790, y), pixel(800, y),
    ]
    for pos, coord in enumerate(box):
        if coord == white:
            report.append(True)
            break

    # Legenda encontrada
    if len(report) > 0:
        pass
    # Imagem sem legenda
    else:
        moveTo(*editor_del_icon)
        sleep(.3)
        click()
        # hotkey('delete')
        # sleep(.7)
        # hotkey('enter')
    report.clear()
    hotkey('right')

    # if color_tuple == white:
    #     counter += 1
    #     print(f'legenda {counter}')
    #     hotkey('right')
    # else:
    #     hotkey('delete')
    #     hotkey('enter')

    # if locateOnScreen('letter_i.png') is not None:
    #     print('Letra I encontrada')
    # if locateOnScreen('letter_e.png') is not None:
    #     print('Letra E encontrada')
    # if locateOnScreen('letter_o.png') is not None:
    #     print('Letra O encontrada')
    # if locateOnScreen('letter_u.png') is not None:
    #     print('Letra U encontrada')
