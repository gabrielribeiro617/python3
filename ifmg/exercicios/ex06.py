lista_preco = list()
soma = float(0.0)

print('Informe o preço dos produtos: ')

for cont in range(5):
    preco = float(input(f'Produto {cont + 1}: '))
    soma += preco
    lista_preco.append(preco)

media = float(soma / 5)
print('Preços acima da média:')

for i, preco in enumerate(lista_preco):
    if preco >= media:
        print(f'Produto {i + 1}: {preco}')
