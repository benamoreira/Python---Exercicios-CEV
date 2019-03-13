jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do Jogador: '))
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
c = 1
while c <= jogos:
    gols.append(int(input(f'Quantos gols na {c}ª partida? ')))
    c+=1
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('=-'*31)
print(jogador)
print('=-'*31)
for k, v in jogador.items():
    print(f'O {k} tem o valor {v}')
print('=-'*29)
print(f'O jogador {jogador["nome"]} joou {jogos} vezes!')
for i, v in enumerate(gols):
    print(f'   => Na {i+1}ª partida, fez {v} gols. ')
print(f'Fez um total de {jogador["total"]} gols!')
