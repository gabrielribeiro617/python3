n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

p = bool(n1 > n2)
q = bool(n1 != n2)
r = bool(not (p or q) and (not p))

print(f'p = {p}')
print(f'q = {q}')
print(f'r = {r}')
