from random import randint
tv = int(0)
print('\033[1;97m-=' * 15)
print('\033[1;35m VAMOS JOGAR PAR OU ÍMPAR')
print('\033[1;97m-=\033[m' * 15)
while True:
    nj = int(input('Diga um valor: '))
    nc = int(randint(0, 10))
    sn = nj + nc
    esc = esj = str(' ')
    while esj not in 'PI':
        esj = str(input('Par ou Ímpar: \033[1m[P/I]\033[m ')).upper().strip()[0]
    print('\033[1;97m--\033[m' * 15)
    if sn % 2 == 0: esc = 'PAR'
    else: esc = 'IMPAR'
    print(f'\033[1mVocê jogou {nj} e o computador {nc}. Total de {sn} \033[4mDEU {esc}\033[m')
    print('\033[1;97m--\033[m' * 15)
    if esj == esc[0]:
        print('\033[1;32mVOCÊ VENCEU!\033[m\nVamos jogar novamente...')
        print('\033[1;97m-=\033[m' * 15)
        tv += 1
    else:
        print('\033[1;31mVOCÊ PERDEU!\033[m')
        print('\033[1;97m-=\033[m' * 15)
        print(f'\033[1;97;41mGAME OVER! Você venceu {tv} vezes.\033[m')
        break
