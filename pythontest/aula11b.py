n = 'Gabriel'
c = {'limpa':'\033[m',
     'azul':'\033[4;34m',
     'amarelo':'\033[33m',
     'vermelho':'\033[31m',
     'pretoebranco':'\033[1;30;107m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(c['pretoebranco'], n, c['limpa']))
