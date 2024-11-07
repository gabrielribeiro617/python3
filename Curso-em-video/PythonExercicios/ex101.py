def voto(nasc):
    from datetime import datetime
    idade = datetime.now().year - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade <= 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPICIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('--' * 20)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
