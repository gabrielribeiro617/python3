from random import randint
from time import sleep
com = randint(0, 10)
con = int(1)
print('\033[33m-=-' * 20)
print('  \033[1;34mVou pensar em um número entre 0 e 10. Tente adivinhar...')
print('\033[33m-=-' * 20)
jog = int(input('\033[mEm que número eu pensei? '))
print('\033[35mPROCESSANDO...')
sleep(1)
while jog != com:
    if jog < com:
        jog = int(input('\033[1;33mMais... Tente adivinhar novamente: '))
    else:
        jog = int(input('\033[1;33mMenos... Tente adivinhar novamente: '))
    con += 1
print('\033[1;32mPARABÉNS! Você conseguiu me vencer!')
if con == 1:
    print('VOCÊ ACERTOU DE PRIMEIRA!!!')
else:
    print(f'Mas você precisou de {con} tentativa(s).')
