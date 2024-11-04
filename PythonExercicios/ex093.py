jogo = {'nome': '', 'gols': 0, 'total': 0}
qntGols = list()
jogo['nome'] = str(input('Nome do Jogador: ')).capitalize()
qnt = int(input(f'Quantas partidas {jogo['nome']} jogou? '))
for c in range(0, qnt):
    qntGols.append(int(input(f'   Quantos gols na partida {c}? ')))
jogo['total'] = sum(qntGols)
jogo['gols'] = qntGols
print('-=' * 30)
print(jogo)
print('-=' * 30)
for k, v in jogo.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogo['nome']} jogou {qnt} partidas.')
for pos, gols in enumerate(qntGols):
    print(' ' * 2, f'=> Na partida {pos}, fez {gols} gols.')
print(f'Foi um total de {jogo['total']} gols.')
