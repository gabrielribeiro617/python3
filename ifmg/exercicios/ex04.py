from time import sleep

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def arquivoCriar(nome):
    try:
        a = open(nome, 'wt')
        a.close()
    except:
        print(f'Erro ao criar arquivo {nome}!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def cadastro(arq, expressao, resultado):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir arquivo!')
    else:
        try:
            a.write(f'{expressao};{resultado}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            a.close()

def arquivoLer(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro na leitura do arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'-> {dado[0]} = {dado[1]}')
    finally:
        a.close()

def titulo(txt):
    print('==' * 20)
    print(txt.center(40))
    print('==' * 20)


# Programa Principal
arquivo = 'historico_calculos.txt'

if not arquivoExiste(arquivo):
    arquivoCriar(arquivo)
    
titulo('CALCULADORA')

while True:
    print('[ h -> ver histórico | s - > sair ]')
    print('Insira a sua expressão:')
    exp = input('=> ').lower()
    sleep(0.5)
    if exp == 'h':
        titulo('HISTÓRICO')
        arquivoLer(arquivo)
        sleep(0.5)
        print('--' * 20)
        continue
    elif exp == 's':
        break
    else:
        res = eval(exp)
        cadastro(arquivo, exp, res)
        print(f'= {res}')
        while True:
            cont = str(input('Quer continuar [s/n]? ')).lower().strip()[0]
            if cont in 'sn':
                sleep(0.5)
                print('--' * 20)
                break;
        if cont in 'n':
            break

sleep(0.5)
titulo('PROGRAMA ENCERRADO')
