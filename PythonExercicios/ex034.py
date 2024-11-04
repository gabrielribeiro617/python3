s = float(input('Qual é o salário do funcionário? R$'))
if s > 1250:
    a = s * 1.10
else:
    a = s * 1.15
print('Quem ganhava R${:.2f} passa a ganhar \033[1;32mR${:.2f}\033[m agora.'.format(s, a))
