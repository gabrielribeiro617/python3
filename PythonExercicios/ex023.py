from time import sleep
n = int(input('\033[1;36mDigite um número: '))
print('\033[1;36mAnalisando o número: {}...'.format(n))
sleep(2)
print('\033[33mUnidade: {}'.format(n // 1 % 10))
print('\033[33mDezena: {}'.format(n // 10 % 10))
print('\033[33mCentena: {}'.format(n // 100 % 10))
print('\033[33mMilhar: {}'.format(n // 1000 % 10))
