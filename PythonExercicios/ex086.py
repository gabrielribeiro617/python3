mat = [[], [], []]
for i in range(0, 3):
    for c in range(0, 3):
        mat[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))
print('-=' * 30)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[i][c]:^5}]', end=' ')
    print()
