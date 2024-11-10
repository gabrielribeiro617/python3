from time import sleep

dados = list()
sal_novo = float

print('==' * 30)
print('  DADOS DOS FUNCIONÁRIOS')
print('==' * 30)

for cont in range(3):
    print(f'Funcionario {cont + 1}:')
    nome = str(input(' Nome: ')).title().strip()
    salario = float(input(' Salário: R$ '))
    if salario <= 2000:
        sal_novo = salario * 1.20
    elif 2000 < salario <= 5000:
        sal_novo = salario * 1.15
    else:
        sal_novo = salario * 1.05
    funcionarios = (nome, salario, sal_novo)
    dados.append(funcionarios)
    if cont != 2:
        print('--' *30)

sleep(0.5)
print('==' * 30)
print('  PROMOÇÃO')
print('==' * 30)
sleep(0.5)

for i, func in enumerate(dados):
    nome, salario, sal_novo = func
    print(f'Funcionário {i + 1}:')
    print(f' Aumento Salarial: R$ {(sal_novo - salario):.2f}')
    print(f' Salário Final: R$ {sal_novo:.2f}')
    if i != 2:
        print('--' * 30)
    sleep(0.5)

print('==' * 30)
sleep(0.5)
print('FUNCIONÁRIOS COM SALÁRIO MENOR QUE R$ 2000,00:')
print('==' * 30)

for i, func in enumerate(dados):
    nome, salario, sal_novo = func
    if sal_novo < 2000:
        print(f' Funcionário {i + 1}: {nome}')
    sleep(0.5)

print('--' * 30)
