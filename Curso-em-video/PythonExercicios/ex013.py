s = float(input('\033[1;32mQual é o seu salário? R$'))
ns = 1.15 * s
print('\033[33mVocê teve um aumento! Agora o seu salário é R${:.2f}'.format(ns))
