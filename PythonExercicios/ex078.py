val = list()
for c in range(0,5):
    val.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-=' * 40)
print(f'Você digitou os valores {val}')
print(f'O maior valor digitado foi {max(val)} nas posições', end=' ')
for cont, v in enumerate(val):
    if v == max(val):
        print(cont, end='... ')
print(f'\nO menor valor digitado foi {min(val)} nas posições', end=' ')
for cont, v in enumerate(val):
    if v == min(val):
        print(cont, end='... ')
