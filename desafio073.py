times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG',
         'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians',
         'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')

primeiros = times[0:5]
print('Os 5 primeiros são: ', primeiros)
ultimos = times[16:21]
print('Os 4 ultimos são: ', ultimos)
ordem = sorted(times)
print('Ordem Alfabética: ', ordem)
chape = 'Chapecoense'
print(f'A {chape} está na {times.index(chape)}ª posição.')