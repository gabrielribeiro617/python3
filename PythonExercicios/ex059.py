from time import sleep
ma = float(0)
print('\033[1;32m-=-' * 20)
print(f'\033[1;34m DESAFIO 059')
print('\033[1;32m-=-' * 20)
n1 = float(input('\033[mPrimeiro valor: '))
n2 = float(input('Segundo valor: '))
print('\033[1;97m-=-' * 15, '\n\033[1;34mOPÇÕES:')
print('\033[1;97m[ 1 ]\033[m SOMAR\n\033[1;97m[ 2 ]\033[m MULTIPLICAR\n'
      '\033[1;97m[ 3 ]\033[m MAIOR\n\033[1;97m[ 4 ]\033[m NOVOS VALORES\n'
      '\033[1;97m[ 5 ]\033[m SAIR DO PROGRAMA')
e = int(input('Qual você escolhe?'))
while e != 5:
    if e == 1:
        print(f'\033[1;97m{n1} + {n2} = {n1 + n2}')
        print('\033[1;97m---' * 7)
        e = int(input('\033[mO que quer fazer agora? '))
    elif e == 2:
        print(f'\033[1;97m{n1} x {n2} = {n1 * n2}')
        print('\033[1;97m---' * 7)
        e = int(input('\033[mO que quer fazer agora? '))
    elif e == 3:
        if n1 > n2:
            ma = n1
            print(f'\033[1;97m{ma} é maior que {n2}.')
            print('\033[1;97m---' * 7)
            e = int(input('\033[mO que quer fazer agora? '))
        elif n2 > n1:
            ma = n2
            print(f'\033[1;97m{ma} é maior que {n1}.')
            print('\033[1;97m---' * 7)
            e = int(input('\033[mO que quer fazer agora? '))
        else:
            print('\033[1;97mOs números são iguais.')
            print('\033[1;97m---' * 7)
            e = int(input('\033[mO que quer fazer agora? '))
    elif e == 4:
        n1 = float(input('\033[mPrimeiro valor: '))
        n2 = float(input('Segundo valor: '))
        print('\033[1;97m---' * 10)
        e = int(input('\033[mO que quer fazer agora? '))
    elif e > 1 or e < 5:
        e = int(input('\033[1;31mERRO! tente novamente: '))
print('\033[1;33mSAINDO...')
sleep(1)
print('\033[1;35mVOCÊ SAIU DO PROGRAMA')
