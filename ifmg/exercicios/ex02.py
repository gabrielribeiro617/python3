from math import pow, sqrt 

print('Informe os termos da equação Ax² + Bx + C')

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

if a == 0:
    print("Não é um aquação de segundo grau")
else:
    delta = float(pow(b, 2) - 4 * a * c)
    if delta < 0:
        print('A equação não possui raízes')
    elif delta == 0:
        x1 = b * (-1) / 2 * a
        print(f'A equação possui uma única raíz: {x1:.2f}')
    else:
        x1 = float(b * (-1) + sqrt(delta) / 2 * a)
        x2 = float(b * (-1) - sqrt(delta) / 2 * a)
        print('A equação possui duas raízes:')
        print(f'x1 = {x1:.2f}')
        print(f'x2 = {x2:.2f}')
    