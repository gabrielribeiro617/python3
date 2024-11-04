from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 20)
    if passo < 0:
        passo *= - 1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if inicio > fim:
        passo *= - 1
        fim -= 1
    else:
        fim += 1
    sleep(0.5)
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.25)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
