from random import choice
a1 = str(input('\033[1;35mPrimeiro aluno: '))
a2 = str(input('\033[1;35mSegundo aluno: '))
a3 = str(input('\033[1;35mTerceiro aluno: '))
a4 = str(input('\033[1;35mQuarto aluno: '))
l = [a1,a2,a3,a4]
print('\033[33mO aluno sorteado foi {}'.format(choice(l)))
