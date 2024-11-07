n = int(input('Digite um número para ver a tabuada: '))
print('\033[1m---' * 12)
for c in range(1, 11):
    print(f'\033[1;97m{n} x {c:2} = {n*c}')
