n = int(1)
par = imp = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            imp += 1
print(f'Você digitou {par} número(s) par(es) e {imp} número(s) ímpar(es).')
