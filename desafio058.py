from random import randint
numpc = randint(0,10)
print(numpc)

chute = 0
contachute = 0

while chute != numpc:
    chute = int(input('Qual seu paupite?'))
    contachute += 1

print('Voçê precisou de {} chutes para acertar!'.format(contachute))