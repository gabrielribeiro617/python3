from datetime import date
print('\033[33m-=-' * 20)
print('\033[1;34m ALISTAMENTO MILITAR')
print('\033[33m-=-' * 20)
n = int(input('\033[mEm que ano você nasceu? '))
i = date.today().year - n
print('Quem nasceu em {} tem {} anos em {}.'.format(n, i, date.today().year))
print('\033[1m---' * 10)
s = str(input('\033[mQual é o seu sexo? ')).upper().strip()
if s == 'FEMININO':
    print('\033[1;32mVocê não precisa se alistar!')
elif s == 'MASCULINO':
    if i > 18:
        print('\033[31mVocê já deveria ter se alistado há {} ano(s).'.format(i - 18))
        print('\033[1;31mSeu alistamento foi em {}.'.format(n + 18))
    elif i < 18:
        print('\033[33mAinda falta(m) {} ano(s) para o alistamento.'.format(18 - i))
        print('\033[1;33mSeu alistamento será em {}.'.format(n + 18))
    else:
        print('\033[1;32mVocê tem que se alistar imediatamente!')
else:
    print('\033[1;31mERRO! Essa opção não existe!')

