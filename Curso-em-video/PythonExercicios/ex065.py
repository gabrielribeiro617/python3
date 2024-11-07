res = bool(False)
tn = ts = n = int(0)
nma = nme = int(n)
while res is not True:
    n = int(input('Digite um número: '))
    ns = str(input('Quer continuar? \033[1m[S/N]\033[m ')).upper().strip()[0]
    print('\033[1;97m---\033[m' * 15)
    tn += 1
    ts += n
    if n >= nma:
        nma = n
    else:
        nme = n
    if ns == 'N':
        res = True
print(f'\033[1;35mVocê digitou {tn} números e a média foi {ts / tn}'
      f'\nO maior valor foi {nma} e o menor foi {nme}')
