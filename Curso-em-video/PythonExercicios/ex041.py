from datetime import date
a = int(input('Em que ano você nasceu? '))
i = date.today().year - a
print('O atleta te {} anos.'.format(i))
if i <= 9:
    print('\033[1mClassificação: \033[1;34mMIRIM')
elif i <= 14:
    print('\033[1mClassificação: \033[1;31mINFANTIL')
elif i <= 19:
    print('\033[1mClassificação: \033[1;33mJUNIOR')
elif i <= 20:
    print('\033[1mClassificação: \033[1;32mSÊNIOR')
else:
    print('\033[1mClassificação: \033[1;35mMASTER')
