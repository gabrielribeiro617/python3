from math import hypot
co = float(input('\033[1;35mDigite o cateto oposto: '))
ca = float(input('\033[1;35mDigite o cateto adjacente: '))
h = hypot(co, ca)
print('\033[33mO comprimento da hipotenusa desse triângulo retangulo é {:.2f}'.format(h))
