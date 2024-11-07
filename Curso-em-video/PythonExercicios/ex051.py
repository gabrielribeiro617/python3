p = int(input('Primeiro termo da PA: '))
r = int(input('Razão: '))
dec = p + (10 - 1) * r
print('\033[1m---' * 10)
for c in range(p, dec + r, r):
    print(f'{c}', end=' ')
print('ACABOU')
