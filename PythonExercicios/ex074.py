from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
     randint(0, 10))
print(f'Número sorteados: ', end='')
for c in n:
    print(c, end=' ')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
