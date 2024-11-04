from utilidadesCeV import string, dado, arquivo

arq = 'cursoemvideo.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)
while True:
    resp = dado.menu(['Ver pessoas cadastradas',
               'Cadastrar nova Pessoa',
               'Sair do Sistema'])
    if resp == 1:
        arquivo.lerArquivo(arq)
    elif resp == 2:
        string.titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = dado.leiaInt('Idade: ')
        arquivo.cadastro(arq, nome, idade)
    elif resp == 3:
        string.titulo('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
