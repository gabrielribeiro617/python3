n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[4;32mPRIMEIRO\033[m valor é maior.')
elif n1 == n2:
    print('Não existe valor maior, \033[4;32mos dois são iguais.')
else:
    print('O \033[4;32mSEGUNDO\033[m valor é maior.')
