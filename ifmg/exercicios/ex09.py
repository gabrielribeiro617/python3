soma = float(0)
lista_produtos = list()

print('Informe os dados do produto:')
for cont in range(5):
    print(f'Produto {cont + 1}:')
    nome = str(input('Nome: ')).title().strip()
    preco = float(input('Preço: R$ '))
    print('--' * 20)
    soma += preco
    produto = [nome, preco]
    lista_produtos.append(produto)
print('==' * 20)

media = float(soma / 5)
print(f'Preço médio: R$ {media:.2f}')
print('Os produtos com preço acima da média são:')
for produto in lista_produtos:
    if produto[1] >= media:
        print(f'Produto: {produto[0]}')
        print(f'Preço: R$ {produto[1]}')
        print('--' * 20)
