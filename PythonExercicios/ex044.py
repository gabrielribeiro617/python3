print('\033[33m=' * 10, '\033[1;34mLOJAS GUANABARA', '\033[33m=' * 10 )
p = float(input('\033[mQual é o preço do produto? R$'))
print('\033[1;35mFORMAS DE PAGAMENTO\033[m')
print('\033[1;97m[ 1 ]\033[m À vista no dinheiro/cheque: 10% de desconto')
print('\033[1;97m[ 2 ]\033[m À vista no cartão: 5% de desconto')
print('\033[1;97m[ 3 ]\033[m Em até 2x no cartão: preço normal')
print('\033[1;97m[ 4 ]\033[m 3x ou mais no cartão: 20% de juros')
e = int(input('Qual é a opção? '))
print('\033[1m---' * 10)
if e == 1:
    print('\033[1;97mValor a ser pago: R${:.2f}'.format(p * 0.90))
elif e == 2:
    print('\033[1;97mValor a ser pago: R${:.2f}'.format(p * 0.95))
elif e == 3:
    print('\033[1;97mValor a ser pago: 2x de R${:.2f}'.format(p / 2))
elif e == 4:
    x = int(input('\033[mQuantas parcelas? '))
    print('\033[1;97mValor a ser pago: \033[1;97m{}x de R${:.2f}'.format(x, (p * 1.20)/ x))
    print('\033[4;33mSua compra de R${:.2f} vai custar R${:.2f} no final'.format(p, p * 1.20))
elif e < 4 or e > 1:
    print('\033[1;31mERRO! OPÇÃO INVÁLIDA.')