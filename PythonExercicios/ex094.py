pessoas = {'nome': '', 'sexo': '', 'idade': 0}
grupo = list()
medId = float(0)
while True:
    pessoas['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    medId += pessoas['idade']
    grupo.append(pessoas.copy())
    res = str(' ')
    while True:
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if res in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if res == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'B) A média de idade é de {medId / len(grupo):5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for pess in grupo:
    if pess['sexo'] == 'F':
        print(pess['nome'], end=' ')
print('\nD) A lista de pessoas que estão acima da média:')
for pess in grupo:
    if pess['idade'] > medId / len(grupo):
        print('   ', end='')
        for k, v in pess.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
