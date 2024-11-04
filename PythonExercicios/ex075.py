num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'\033[97mVocê digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vez(es)')
if 3 not in num:
    print('O valor 3 não foi digitado em nenhuma posição')
else: print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
