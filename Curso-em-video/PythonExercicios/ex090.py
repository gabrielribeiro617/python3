boletim = dict()
boletim['nome'] = str(input('Nome: ')).capitalize().strip()
boletim['média'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['média'] >= 7:
    boletim['situação'] = 'Aprovado'
elif boletim['média'] <= 5:
    boletim['situação'] = 'Reprovado'
else: boletim['situação'] = 'Recuperação'
print('-=' * 30)
for k, v in boletim.items():
    print(' ' * 2, f'- {k} é igual a {v}')
