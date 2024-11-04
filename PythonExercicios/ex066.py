tn = s = int(0)
while True:
    n = int(input('Digite um número: \033[1m[999 para parar]\033[m '))
    if n == 999:
        break
    tn += 1
    s += n
print(f'\033[1;97mForam digitados {tn} números e a soma deles é {s}.')
