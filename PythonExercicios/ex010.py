r = float(input('\033[1;32mQuantos reais você tem na carteira? R$'))
d = r/3.27
print('\033[33mVocê pode comprar US${:.2f} com R${:.2f}'.format(d,r))
