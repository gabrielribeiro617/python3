estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print('--' * 20)
for est in brasil:
    for val in est.values():
        print(val, end=' ')
    print()
