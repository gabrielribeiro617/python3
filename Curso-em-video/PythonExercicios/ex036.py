c = float(input('Qual é o valor da casa? R$'))
s = float(input('Qual é o valor do seu salário? R$'))
a = int(input('Quantos anos de financiamento? '))
p = float((c / a) / 12)
print('\033[33mPara pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(c, a, p))
if p <= s * 0.3:
    print('\033[1;32mEMPRÉSTIMO ACEITO!')
else:
    print('\033[1;31mEMPRÉSTIMO NEGADO!')
