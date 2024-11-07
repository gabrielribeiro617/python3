v = float(input('Qual é a velocidade atual do seu carro? '))
if v > 80:
    print('\033[1;31mMULTADO! Você excedeu o limite que é de 80km/h.')
    print('Você deve pagar uma multa de \033[1;33mR${:.2f}!'.format((v - 80) * 7))
print('\033[1;32mTenha um bom dia! Dirija com segurança!')
