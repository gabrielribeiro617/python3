jogo = {'nome': '', 'gols': 0, 'total': 0}
jogadores = list()
qntGols = list()
while True:
    print('--' * 20)
    jogo['nome'] = str(input('Nome do Jogador: ')).capitalize()
    qnt = int(input(f'Quantas partidas {jogo['nome']} jogou? '))
    for c in range(0, qnt):
        qntGols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
        jogo['total'] = sum(qntGols)
    jogo['gols'] = qntGols[:]
    jogadores.append(jogo.copy())
    jogo['total'] = 0
    qntGols.clear()
    while True:
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if res in 'SN':
            break
        print('ERRO! Responda apenas S e N.')
    if res == 'N':
        break
print('-=' * 30)
print('cod', end=' ')
for ind in jogo.keys():
    print(f'{ind:<15}', end='')
print()
print('--' * 20)
for pos, jd in enumerate(jogadores):
    print(f'{pos:<3}', end='')
    for d in jd.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('--' * 20)
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    elif busca >= len(jogadores) or busca < 0:
        print(f'ERRO! Não existe jogador com código {busca}! Tente novamente.')
    elif busca < len(jogadores) or busca >= 0:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for cont in range(0, len(jogadores[busca]["gols"])):
            print(' ' * 2, f'No jogo {cont + 1} fez {jogadores[busca]["gols"][cont]} gols.')
print('<< VOLTE SEMPRE >>')
