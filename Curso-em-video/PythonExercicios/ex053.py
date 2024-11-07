f1 = str(input('Digite um frase: ')).upper().strip()
r = ''.join(f1.split())[len(f1)::-1]
f2 = ''.join(f1.split())
print(f'O inverso de {f2} é {r}.')
if f2 == r:
    print('\033[1;32mA frase digitada 'f'\033[4mé um PALÍNDROMO!')
else:
    print('\033[1;31mA frase digitada 'f'\033[4mNÃO é um PALÍNDROMO!')
