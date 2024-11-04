boletim = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = float((n1 + n2)/ 2)
    boletim.append([nome, [n1, n2, med]])
    res = str(' ')
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if res in 'N':
        break
print('-=' * 30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('--' * 15)
for pos, aluno in enumerate(boletim):
    print(f'{pos:<4}{aluno[0]:<10}{aluno[1][2]:>8.1f}')
print('--' * 25)
while True:
    res = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    if 0 <= res <= len(boletim) - 1:
        print(f'Notas de {boletim[res][0]} são {boletim[res][1][:2]}')
        print('--' * 25)
    elif res == 999:
        break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
