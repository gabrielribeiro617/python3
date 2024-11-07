def fatorial(numero=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opicional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número numero.
    """
    print('--' * 20)
    f = 1
    for c in range(numero, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


help(fatorial)
print(fatorial(5, True))
