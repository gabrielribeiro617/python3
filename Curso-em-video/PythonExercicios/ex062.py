pri = int(input('Primeiro termo da PA: '))
raz = int(input('Razão: '))
cont = int(0)
tot = int(10)
while cont < tot:
    print(f'\033[1;97m{pri}\033[m', end=' - ')
    pri += raz
    cont += 1
    if cont == tot:
        print('\033[1;97mPAUSA\033[m')
        print('\033[1m---\033[m' * 10)
        tot += int(input('Você quer mostrar mais quantos termos? '))
print('\033[1;97m-=-\033[m' * 10)
print(f'\033[1;35mProgressão finalizada com {cont} termos mostrados.')
