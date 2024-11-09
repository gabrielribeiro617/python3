lista = [1,2,4,5]

print(lista)

val1 = int(input('Digite um número para pôr no final da lista: '))
lista.append(val1) # Adiciona o valor dentro de () à lista.
print(lista)

val2 = int(input('Digite um número para pôr na posicao 2: '))
lista.insert(2, val2)
print(lista)

posicao = int(input('Digite a posição que deseja remover: '))
lista.pop(posicao)
print(lista)

resp = str(input('Deseja apagar a lista [s/n]? ')).lower().strip()[0]

if resp in 's':
    lista.clear()
    print(lista)
