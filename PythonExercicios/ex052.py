n = int(input('Digite um número: '))
p = 0
for c in range(1, n + 1):
    if c == 1 or c == n:
        if n % c == 0:
            p += 1
            print(f'\033[33m{c}\033[m', end=' ')
    elif c > 1 or c < n:
        if n % c == 0:
            p += 1
            print(f'\033[31m{c}\033[m', end=' ')
print('\n', '\033[1;35m-=-\033[m' * 10)
print(f'\033[1mO número {n} foi divisível {p} vezes.')
if n > 1 and p == 2:
    print(f'\033[1;32mE por isso É PRIMO.')
else:
    print(f'\033[1;31mE por isso NÃO É PRIMO.')
