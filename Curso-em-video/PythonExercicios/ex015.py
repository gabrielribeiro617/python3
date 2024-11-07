d = int(input('\033[1;35mQuantos dias alugados? '))
km = float(input('\033[1;35mQuantos Km rodados? '))
t = (d * 60) + (km * 0.15)
print('\033[33mO total a pagar é de R${:.2f}'.format(t))
