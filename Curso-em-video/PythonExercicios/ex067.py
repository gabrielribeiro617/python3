while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'\033[1;97m{n} x {c:2} = {n * c}\033[m')
    print('\033[1m--\033[m' * 20)
print('\033[1;35mPROGRAMA TABUADA ENCERRADO. Volte sempre!')
