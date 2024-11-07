galera = list()
dado = list()
pmai = pmen = int(0)
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    galera.append(dado[:])
    dado.clear()
    res = str(' ')
    while True:
        res = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if res in 'SN':
            break
    if res in 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(galera)} pessoa(s).')
for c in range(0, len(galera)):
    if c == 0 or galera[c][1] >= pmai:
        pmai = galera[c][1]
    if c == 0 or galera[c][1] <= pmen:
        pmen = galera[c][1]
print(f'O maior peso foi de {pmai:.2f}Kg. Peso de', end=' ')
for c in range(0, len(galera)):
    if galera[c][1] == pmai:
        print(f'[{galera[c][0]}]', end=' ')
print(f'\nO menor peso foi de {pmen:.2f}Kg. Peso de', end=' ')
for c in range(0, len(galera)):
    if galera[c][1] == pmen:
        print(f'[{galera[c][0]}]', end=' ')
