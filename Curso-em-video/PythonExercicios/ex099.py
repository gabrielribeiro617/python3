from time import sleep


def maior(* numeros):
    print('-=' * 30)
    print('Analisando os valores passado...')
    sleep(0.5)
    for valor in numeros:
        print(f'{valor}', end=' ')
        sleep(0.25)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi ', end='')
    if numeros != ():
        print(f'{max(numeros)}.')
    else:
        print('0.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
