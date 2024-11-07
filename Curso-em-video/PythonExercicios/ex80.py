val = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > val[-1]:
        val.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = int(0)
        while pos < len(val):
            if n <= val[pos]:
                val.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {val}')

