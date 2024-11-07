from random import randint


def dobra(lst):
    for pos in range(0, len(lst)):
        lst[pos] *= 2


def soma(* valores): # Função usando desempacotamento
    s = int(0)
    for val in valores:
        s += val
    print(f'Somando os valores {valores} temos {s}.')

    
def lindif():
    print('-=' * 30)


# Programa Principal
valores = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
print(valores) # Valores s/ função
dobra(valores) # Aplicando a função dobra()
print(valores) # Valores c/ função
lindif()
# Usando a função soma() com número inteiros aleatórios
soma(randint(1, 10), randint(1, 10))
soma(randint(1, 10), randint(1, 10), randint(1, 10))
