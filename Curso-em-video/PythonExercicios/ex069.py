t18 = th = m20 = int(0)
while True:
    print('\033[1;97m--\033[m' * 20)
    print('\033[1;35m CADASTRE UMA PESSOA\033[m')
    print('\033[1;97m--\033[m' * 20)
    id = int(input('Idade: '))
    if id > 18:
        t18 += 1
    sx = res = str(' ')
    while sx not in 'MF':
        sx = str(input('Sexo: \033[1m[M/F]\033[m ')).upper().strip()[0]
    if sx == 'M':
        th += 1
    if id < 20 and sx == 'F':
        m20 += 1
    print('\033[1;97m--\033[m' * 20)
    while res not in 'SN':
        res = str(input('Quer continuar? \033[1m[S/N]\033[m ')).upper().strip()[0]
    if res == 'N':
        print('\033[1;97m==\033[m' * 5, end=' ')
        print('\033[1;35mFIM DO PROGRAMA', '\033[1;97m==\033[m' * 5)
        break
print(f'Total de pessoas com mais de 18 anos: {t18}')
print(f'Ao todo temos {th} homem(ns) cadastrado(s)')
print(f'E temos {m20} mulher(es) com menos de 20 anos')
