ma = float(0)
me = float(0)
for c in range(1, 6):
    p = float(input(f'Qual é o peso da {c}ª pessoa em Kg? '))
    if c == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        elif p < me:
            me = p
print('\033[1m-=-' * 10)
print(f'\033[1;97mO maior peso foi de {ma:.1f}Kg.\n'
      f'O menor peso foi de {me:.1f}Kg.')
