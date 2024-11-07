def titulo(txt, cor=0):
    print(cores[cor], end='')
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))
    print(cores[0], end='')


def manual(comando):
    from time import sleep
    titulo(f'Acessando o manual do comando \'{comando}\'', 3)
    sleep(1)
    print(cores[4], end='')
    help(comando)
    print(cores[0], end='')


cores = ('\033[m',
         '\033[0;97;41m',
         '\033[0;97;42m',
         '\033[0;97;44m',
         '\033[0;30;107m')
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    c = str(input('Função ou Biblioteca > ')).lower()
    if c == 'fim':
        titulo('ATÉ LOGO!', 1)
        break
    manual(c)
