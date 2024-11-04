s = 0
tv = 0
for c in range(1, 501, 2):
    if c % 3 == 0 and c % 2 != 0:
        s += c
        tv += 1
print(f'\033[1;97mA soma de todos os {tv} valores ímpares é de {s}.')
