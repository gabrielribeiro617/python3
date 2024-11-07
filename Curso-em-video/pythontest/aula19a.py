pessoas = {'nome': 'Gabriel', 'sexo': 'M', 'idade': 18}
del pessoas['sexo']
pessoas['nome'] = 'Blab'
pessoas['peso'] = 55.7
for k, v in pessoas.items():
    print(f'{k} = {v}')
