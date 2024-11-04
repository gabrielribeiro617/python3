p = float(input('Qual é o seu peso? (Kg) '))
h = float(input('Qual é a sua altura? (m) '))
imc = p / (pow(h, 2))
print('O seu IMC é {:.1f}.'.format(imc))
if imc < 18.5:
    print('\033[1;31mABAIXO DO PESO!')
elif imc < 25:
    print('\033[1;32mPESO IDEAL!')
elif imc < 30:
    print('\033[1;33mSOBREPESO')
elif imc < 40:
    print('\033[1;33mOBESIDADE')
else:
    print('\033[1;31mOBESIDADE MÓRBIDA')
