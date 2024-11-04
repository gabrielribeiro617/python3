def leiaInt(txt):
    print('--' * 20)
    while True:
        num = str(input(txt))
        if num.isnumeric():
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
