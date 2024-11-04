from random import randint
from time import sleep
n = randint(0, 5)
print('\033[33m-=-' * 20)
print('  \033[1;34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m-=-' * 20)
a = int(input('\033[mEm que número eu pensei? '))
print('\033[35mPROCESSANDO...')
sleep(2)
if a == n:
    print('\033[1;32mPARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[1;31mGANHEI! Eu pensei no número {} e não no {}!'.format(n, a))
