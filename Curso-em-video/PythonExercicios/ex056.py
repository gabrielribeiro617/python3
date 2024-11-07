med = int(0)
maid = int(1)
hmaid = {}
m20 = int(0)
for c in range(1, 5):
    print('-' * 5, f'\033[1;97m{c}ª PESSOA\033[m ', '-' * 5)
    nm = str(input('\033[mNome: ')).capitalize().strip()
    id = int(input('Idade: '))
    sx = str(input('Sexo [M/F]: ')).upper().strip()
    med += id
    if id > maid and sx == 'M':
        hmaid[0] = nm
        hmaid[1] = id
    if id < 20 and sx == 'F':
        m20 += 1
print('\033[1m-=-' * 10)
print(f'\033[1;97mA média de idade do grupo é de {med / 4:.0f} anos.')
print(f'O homem mais velho do grupo tem {hmaid[1]} anos e se chama {hmaid[0]}.')
print(f'Há {m20} mulher(es) com menos de 20 anos.')
