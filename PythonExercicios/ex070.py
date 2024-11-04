tp = mep = float(0)
m100 = con = int(0)
nmp = str('')
print('\033[1;97m--\033[m' * 20)
print(' \033[1;34m LOJA SUPER BARATÃO')
print('\033[1;97m--\033[m' * 20)
while True:
    np = str(input('Nome do produto: ')).capitalize().strip()
    p = float(input('Preço: R$'))
    tp += p
    if p > 1000:
        m100 += 1
    con += 1
    if con == 1 or p < mep:
        mep = p
        nmp = np
    res = str(' ')
    while res not in 'SN':
        res = str(input('Quer continuar? \033[1m[S/N]\033[m ')).upper().strip()[0]
    if res in 'N':
        print('\033[1;97m{:-^40}'.format(' \033[1;35mFIM DO PROGRAMA \033[1;97m'))
        break
print(f'\033[mO total da compra foi R${tp:.2f}')
print(f'Temos {m100} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nmp} que custa R${mep:.2f}')
