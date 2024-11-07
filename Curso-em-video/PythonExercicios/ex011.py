l = float(input('\033[1;32mDigite a largura da parede: '))
h = float(input('\033[1;32mDigite a altura da parede: '))
a = l * h
t = a / 2
print('\033[33mSua parede tem a dimensão de {}x{} e sua área é de {:.1f}m².'.format(l,h,a))
print('\033[33mPara pintar essa parede, você precisará de {:.1f}l de tinta.'.format(t))
