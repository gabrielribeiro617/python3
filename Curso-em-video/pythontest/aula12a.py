n = str(input('Digite o seu nome: ')).capitalize().strip()
if n == 'Gabriel':
    print('Que nome bonito!')
elif n == 'Pedro' or n == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif n in 'Maria Clara Lara':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(n))
