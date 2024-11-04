d = int(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de \033[33m{}Km\033[m.'.format(d))
if d <= 200:
    print('E o preço da passagem será de \033[32mR${:.2f}'.format(d * 0.5))
else:
    print('E o preço da passagem será de \033[32mR${:.2f}'.format(d * 0.45))
