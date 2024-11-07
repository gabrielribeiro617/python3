tn = ts = n = int(0)
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        print(f'Você digitou {tn} números e a soma entre eles foi {ts}.')
    tn += 1
    ts += n
