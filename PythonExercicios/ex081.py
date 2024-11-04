val = list()
while True:
    n = (int(input('Digite um número: ')))
    val.append(n)
    res = str(' ')
    while True:
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(val)} elementos.')
val.sort(reverse=True)
print(f'Os valores em ordem decrescente são{val}')
if 5 in val:
    print('O valor 5 faz parte da lista!')
else: print('O valor 5 não foi encontrado na lista!')
