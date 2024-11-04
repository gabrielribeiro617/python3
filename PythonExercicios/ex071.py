tot = c = int(0)
ced = 50
print('\033[1;97m==\033[m' * 20)
print('\033[1;33m{:^40}'.format('BANCO CEV'))
print('\033[1;97m==\033[m' * 20)
vs = int(input('Qual valor você quer sacar? R$'))
while True:
    if vs >= ced:
        vs -= ced
        tot += 1
    else:
        if tot > 0:
            print(f'Total de {tot} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot = 0
        if vs == 0:
            break
print('\033[1;97m==\033[m' * 20)
print('\033[1;35mVolte sempre ao BANCO CEV! Tenha um bom dia!')
