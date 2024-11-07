from random import randint
from time import sleep
print('\033[33m-=-' * 20)
print(' \033[1;34mJOKENPÔ')
print('\033[33m-=-\033[m' * 20)
j = str('PEDRA PAPEL TESOURA').split()
print('Suas opções:')
print('\033[1;97m[ 0 ]\033[m PEDRA\n\033[1;97m[ 1 ]\033[m PAPEL\n\033[1;97m[ 2 ]\033[m TESOURA')
e = int(input('Qual é a sua jogada? '))
r = randint(0,2)
print('\033[1;31mJO...')
sleep(1)
print('\033[1;33mKEN...')
sleep(1)
print('\033[1;32mPO!!!\033[m')
print('\033[1;97m---' * 10)
print('Computador jogou {}'.format(j[r]))
print('Jogador jogou {}'.format(j[e]))
print('\033[1m---' * 5)
if e == 0:
    if r == 2:
        print('\033[1;32mVOCÊ GANHOU!')
    elif r == 1:
        print('\033[1;31mVOCÊ PERDEU!')
    else:
        print('\033[1;33mEMPATE!')
elif e == 1:
    if r == 0:
        print('\033[1;32mVOCÊ GANHOU!')
    elif r == 2:
        print('\033[1;31mVOCÊ PERDEU!')
    else:
        print('\033[1;33mEMPATE!')
elif e == 2:
    if r == 1:
        print('\033[1;32mVOCÊ GANHOU!')
    elif r == 0:
        print('\033[1;31mVOCÊ PERDEU!')
    else:
        print('\033[1;33mEMPATE!')
