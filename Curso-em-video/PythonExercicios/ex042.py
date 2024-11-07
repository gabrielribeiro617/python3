print('\033[33m-=-' * 20)
print('\033[1;34m Analisador de Trângulos')
print('\033[33m-=-' * 20)
r1 = float(input('\033[mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima \033[1;32mPODEM FORMAR um \033[4mTRIÂNGULO ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO!')
    elif r1 == r2 and r2 != r3 or r1 ==r3 and r3 != r2:
        print('ISÓSCELES!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO!')
else:
    print('Os segmentos acima \033[1;31mNÃO PODEM FORMAR um \033[4mTRIÂNGULO.')
