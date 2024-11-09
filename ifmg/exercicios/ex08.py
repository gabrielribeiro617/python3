print('Informe as datas')
print('Primeira data:')
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
data1 = (ano, mes, dia)

print('Segunda data:')
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
data2 = (ano, mes, dia)

if data1 > data2:
    recente = data1
else: 
    recente = data2
print(f'Data mais recente: {recente[2]}/{recente[1]}/{recente[0]}')
