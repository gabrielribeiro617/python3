print('\033[1;34m-=' * 20)
print('\033[1;35m SEQUÊNCIA DE FIBONACCI:')
print('\033[1;34m-=\033[m' * 20)
nt = int(input('Quantos termos você quer mostrar? '))
print('\033[1m~~' * 15)
n1 = c = int(0)
n2 = int(1)
while c < nt:
    if n1 < n2:
        print(f'\033[1;97m{n1}', end=' - ')
        n1 += n2
        c += 1
    else:
        print(f'\033[1;97m{n2}', end=' - ')
        n2 += n1
        c += 1
print('\033[1;32mFIM\033[m')
print('\033[1m~~' * 15)
