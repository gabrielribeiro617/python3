s = int(0)
v = int(0)
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        v += 1
print('\033[1m---' * 12)
print(f'\033[1;97mVocê informou {v} número(s) par(es) e a soma foi {s}.')
