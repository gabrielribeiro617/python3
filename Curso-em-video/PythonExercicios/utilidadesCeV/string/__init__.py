def titulo(txt):
    print('\033[1m==' * 25)
    print(txt.center(50))
    print('==' * 25, end='')
    print('\033[m')

def linha():
    print('--' * 25)
