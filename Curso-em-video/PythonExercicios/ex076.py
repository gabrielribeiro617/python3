pxp = ('Lápis', 1.75,
       'Borracha', 2.00,
       'Caderno', 15.90,
       'Estojo', 25.00,
       'Transferidor', 4.20,
       'Compasso', 9.99,
       'Mochila', 120.32,
       'Canetas', 22.30,
       'Livro', 34.90)
print('--' * 20)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('--' * 20)
for c in range(0, len(pxp), 2):
    print('{:.<30}R$ {:>6.2f}'.format((pxp[c]), pxp[c + 1]))
print('--' * 20)
