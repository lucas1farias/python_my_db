

def ink(color: str = 'blue', text: str = 'texto'):
    # keys = conditions / values = actions of the conditions
    colors = {
        'black': '\033[1:30m' + text + '\033[m',
        'red': '\033[1:31m' + text + '\033[m',
        'green': '\033[1:32m' + text + '\033[m',
        'yellow': '\033[1:33m' + text + '\033[m',
        'blue': '\033[1:34m' + text + '\033[m',
        'purple': '\033[1:35m' + text + '\033[m',
        'cyan': '\033[1:36m' + text + '\033[m',
        'gray': '\033[1:37m' + text + '\033[m',
    }

    for key in colors:
        if color == key:
            return colors[key]


def ink_random(the_text: str):
    from random import choice

    box: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m',
        '\033[1:33m', '\033[1:34m', '\033[1:35m',
        '\033[1:36m', '\033[1:37m', '\033[1:38m',
    )

    return f"{choice(box)}{the_text}{box[-1]}"


if __name__ == '__main__':
    print(ink(color='blue', text='Python'))
    print('\033[1:30m' + 'py' + '\033[1:38m')
    print('\033[1:31m' + 'py' + '\033[1:38m')
    print('\033[1:32m' + 'py' + '\033[1:38m')
    print('\033[1:33m' + 'py' + '\033[1:38m')
    print('\033[1:34m' + 'py' + '\033[1:38m')
    print('\033[1:35m' + 'py' + '\033[1:38m')
    print('\033[1:36m' + 'py' + '\033[1:38m')
    print('\033[1:37m' + 'py' + '\033[1:38m')
