val = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in val:
        val.append(n)
        print('Valor adicionado com sucesso...')
    else: print('Valor duplicado! Não vou adicionar...')
    res = str(' ')
    while True:
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if res in 'SN':
            break
        else: print('Tente novamente.', end=' ')
    if res in 'N':
        break
print('-=' * 40)
val.sort()
print(f'Você digitou os valores {val}')
