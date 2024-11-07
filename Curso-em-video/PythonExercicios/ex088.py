from random import randint
from time import sleep
sorteio = list()
jog = list()
print('--' * 20)
print(f'{'JOGA NA MEGA SENA':^40}')
print('--' * 20)
res = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, res):
    for c in range(0, 6):
        val = randint(1, 60)
        if val not in jog:
            jog.append(val)
    jog.sort()
    sorteio.append(jog[:])
    jog.clear()
print('-=' * 4, f' <SORTEANDO {res} JOGOS> ', '-=' * 4)
for c in range(0, res):
    sleep(0.5)
    print(f'Jogo {c+1:^2}: {sorteio[c]}')
print('{:-^40}'.format(' < BOA SORTE! > '))
