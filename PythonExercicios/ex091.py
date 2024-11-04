from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
       'jogador2': randint(1, 6),
       'jogador3': randint(1, 6),
       'jogador4': randint(1, 6)}
rank = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(' ' * 2, f'O {k} tirou {v} no dado.')
    sleep(0.5)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' ' * 2, f'== RANKING DOS JOGADORES ==')
for cont, val in enumerate(rank):
    print(' ' * 3, f'{cont + 1}º lugar: {val[0]} com {val[1]}.')
    sleep(0.5)
