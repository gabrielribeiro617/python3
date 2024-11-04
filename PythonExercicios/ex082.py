val = list()
par = list()
imp = list()
while True:
    val.append(int(input('Digite um valor: ')))
    res = str(' ')
    while True:
        res = (str(input('Quer continuar [S/N]? '))).upper().strip()[0]
        if res in 'SN':
            break
    if res in 'N':
        break
print('-=' * 30)
print(f'A lista completa é {val}')
for v in val:
    if v % 2 == 0:
        par.append(v)
    else: imp.append(v)
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {imp}')
