resto = int(1)

while True:
    try:
        n1 = int(input('Informe o primeiro número: '))
        n2 = int(input('Informe o segundo número: '))
    except Exception as e:
        print(type(e))
        print(f'Ocorreu um erro! Tente novamente')
    else:
        print(f'Calculando o MDC de {n1} e {n2}...')
        break

while True:
    if n1 < 1 or n2 < 1:
        print('Números inválidos para MDC!')
        break

    resto = int(n1 % n2)
    
    print(f'numero 1: {n1}, numero 2: {n2}, resto: {resto}')
    print('--' * 20)

    if resto == 0:
        print(f'O MDC é: {n2}')
        break
    else:
        n1 = n2
        n2 = resto

    print(f'numero 1: {n1}, numero 2: {n2}')
    print('==' * 20)
