n = int(input('\033[35mMe diga um número qualquer:\033[m '))
if n % 2 == 0:
    print('{} é um número \033[34mPAR'.format(n))
else:
    print('{} é um número \033[34mÍMPAR'.format(n))
