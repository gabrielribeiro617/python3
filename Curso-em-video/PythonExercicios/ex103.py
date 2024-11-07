def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '' or gols.isnumeric() == False:
        gols = '0'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print('--' * 20)
n = str(input('Nome do Jogador: ')).capitalize()
g = str(input('Número de Gols: '))
print(ficha(n, g))
