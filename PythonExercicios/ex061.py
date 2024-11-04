p = int(input('Primeiro termo da PA: '))
r = int(input('Razão: '))
c = int(0)
print('\033[1m---' * 10)
while c <= 10:
    print(f'{p}', end=' ')
    p += r
    c += 1
print('ACABOU')
