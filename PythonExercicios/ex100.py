from random import randint
from time import sleep


def sorteia(lst):
    print(f'Sorteando 5 da lista:', end=' ')
    sleep(0.5)
    for cont in range(0, 5):
        lst.append(randint(1, 10))
        print(lst[cont], end=' ')
        sleep(0.25)
    print('PRONTO!')


def somaPar(lst):
    soma = int(0)
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lst}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
