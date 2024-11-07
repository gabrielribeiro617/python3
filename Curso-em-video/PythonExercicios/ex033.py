n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
ma = n1
if n2 > ma:
    ma = n2
if n3 > ma:
    ma = n3
me = n1
if n2 < me:
    me = n2
if n3 < me:
    me = n3
print('O maior valor é \033[1;33m{}\033[m'.format(ma))
print('O menor valor é \033[1;33m{}'.format(me))
