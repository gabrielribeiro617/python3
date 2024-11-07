n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/ 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if  m >= 7.0:
    print('\033[1;32mO aluno está APROVADO!')
elif m < 5.0:
    print('\033[1;31mO aluno está REPROVADO!')
else:
    print('\033[1;33mO aluno está em RECUPERAÇÃO')
