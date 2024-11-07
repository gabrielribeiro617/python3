pala = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
        'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in range(0, len(pala)):
    print(f'\nNa palavra {pala[c].upper()} temos ', end='')
    for n in range(0, len(pala[c])):
        if pala[c][n] in 'aeiou':
            print(f'{pala[c][n]}', end=' ')
