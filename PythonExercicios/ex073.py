t = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São Paulo',
     'Bahia', 'Vasco', 'Atlético-MG', 'Internacional', 'Bragantino', 'Athletico-PR',
     'Juventude', 'Criciúma', 'Grêmio', 'Fluminense', 'Corinthians', 'Vitória',
     'Cuiabá', 'Atlético-GO')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {t}')
print('-=' * 20)
print(f'Os 5 primeiros são: {t[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {t[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(t)}')
print('-=' * 20)
print(f'O Grêmio está na {t.index('Grêmio') + 1}ª posição')