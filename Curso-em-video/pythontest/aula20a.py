from random import randint


def soma(a, b):
    print(f'A = {a} e B = {b}')
    print(f'A soma A + B = {a + b}')


def contador(* num): # Função usando desempacotamento
    print(f'Recebi os valores {num} e são ao todo {len(num)} números.')


def lin():
    print('--' * 20)


def lindif():
    print('-=' * 30)


# Programa Principal
    # Usando a função soma()
soma(randint(1, 10), randint(1, 10))
lin()
soma(b=7, a=2)
lindif()
    # Usando a função contador()
contador(2, 1, 7)
lin()
contador(8, 0)
lin()
contador(4, 4, 7, 6, 2)
