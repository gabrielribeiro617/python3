from datetime import datetime
doc = dict()
doc['nome'] = str(input('Nome: ')).capitalize()
ano = int(input('Ano de Nascimento: '))
doc['idade'] = datetime.now().year - ano
doc['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if doc['ctps'] != 0:
    while True:
        doc['contratação'] = int(input('Ano de contratação: '))
        if doc['contratação'] >= ano + 16:
            break
    doc['salário'] = float(input('Salário: R$'))
    doc['aposentadoria'] = (doc['contratação'] - ano) + 35
print('-=' * 30)
for k, v in doc.items():
    print(' ' * 2, f'- {k.capitalize()} tem o valor {v}')
