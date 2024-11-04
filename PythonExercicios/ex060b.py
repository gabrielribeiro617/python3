from math import factorial
c = n = int(input('Digite um número para saber o seu fatorial: '))
print(f'Calculando {n}! = {n} ', end='')
for c in range(n, 0, -1):
    c = c - 1
    print(f'x {c} ', end='')
print(f'= {factorial(n)}')
