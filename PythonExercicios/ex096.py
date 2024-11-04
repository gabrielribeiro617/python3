def area(a, b):
    print(f'A área de um terreno {a}x{b} é de {a * b}m².')


print(' Controle de Terrenos')
print('--' * 10)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
