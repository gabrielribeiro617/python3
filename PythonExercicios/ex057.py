sx = str(input('Digite seu sexo [M/F]: ').upper().strip())[0]
while sx not in 'MF':
        sx = str(input('\033[1;33mPor favor, digite apenas M ou F: ').upper().strip())[0]
print('\033[1;32mOpção válida!')
