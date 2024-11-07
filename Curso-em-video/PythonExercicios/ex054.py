from datetime import date
ma = 0
me = 0
for c in range(1, 8):
    a = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    i = date.today().year - a
    if i >= 21:
        ma += 1
    else:
        me += 1
print('\033[1m---' * 10)
print(f'\033[1;32m{ma} pessoas maiores de idade')
print(f'\033[31m{me} pessoas menores de idade')
