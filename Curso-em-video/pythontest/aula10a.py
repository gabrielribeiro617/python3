n = str(input('Qual é o seu nome? ')).strip()
if n.split()[0] == 'Gabriel':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(n))
