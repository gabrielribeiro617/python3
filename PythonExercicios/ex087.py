mat = [[], [], []]
totpar = totcol = int(0)
for i in range(0, 3):
    for c in range(0, 3):
        mat[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))
        if mat[i][c] % 2 == 0:
            totpar += mat[i][c]
        if c == 2:
            totcol += mat[i][c]
print('-=' * 30)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[i][c]:^5}]', end=' ')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {totpar}.')
print(f'A soma dos valores da terceira coluna é {totcol}.')
print(f'O maior valor da segunda linha é {max(mat[1])}.')
