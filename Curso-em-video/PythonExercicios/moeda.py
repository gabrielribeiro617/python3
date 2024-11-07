def aumentar(n, porc, form=False):
    res = n + (n * (porc / 100))
    return res if form is False else moeda(res)


def diminuir(n, porc, form=False):
    res = n - (n * porc / 100)
    return res if form is False else moeda(res)


def dobro(n, form=False):
    res = n * 2
    return res if form is False else moeda(res)


def metade(n, form=False):
    res = n / 2
    return res if form is False else moeda(res)


def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n, aum, dim):
    print('--' * 20)
    print('RESUMO DO VALOR'.center(40))
    print('--' * 20)
    print(f'Preço analisado:\t\t\t{moeda(n)}')
    print(f'Dobro do preço: \t\t\t{dobro(n, True)}')
    print(f'Metade do preço:\t\t\t{metade(n, True)}')
    print(f'{aum}% de aumento:\t\t\t\t{aumentar(n, aum, True)}')
    print(f'{dim}% de redução:\t\t\t\t{diminuir(n, dim, True)}')
    print('--' * 20)
