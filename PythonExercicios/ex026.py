f = str(input('\033[1;36mEscreva uma frase: ')).strip().upper()
print('\033[33mA letra A aparece {} vezes na frase'.format(f.count('A')))
print('\033[33mA primeira letra A apareceu na posição {}'.format(f.find('A')+1))
print('\033[33mA última letra A apareceu na posição {}'.format(f.rfind('A')+1))
