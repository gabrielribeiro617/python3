n20 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
       'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {n20[n]}.')
        res = str(' ')
        while res not in 'SN':
            res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
            if res in 'S':
                break
        if res in 'N':
            break
    elif n > 20 or n < 0:
        print('Tente novamente.', end=' ')
