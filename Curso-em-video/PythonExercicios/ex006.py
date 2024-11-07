n = int(input('\033[1;32mDigite um número: '))
d = n * 2
t = n * 3
r = pow(n, 0.5)
print('\033[1;32mO seu dobro é \033[1;33m{}'.format(d))
print('\033[1;32mO seu triplo é \033[1;33m{}'.format(t))
print('\033[1;32mA sua raíz quadrada é \033[1;33m{:.2f}'.format(r))
