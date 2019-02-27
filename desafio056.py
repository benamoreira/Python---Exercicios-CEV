media = 0
somaidade = 0
maisVelho = ''
contFem = 0
idadeVelha = 0
totmulher20 = 0

for p in range(1, 5):
    print('-----{}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo {M/F]: ')).strip()
    media += 1
    somaidade += idade
    if p == 1:
        maisVelho = nome
        idadeVelha = idade
    if sexo in 'Mm' and idade > idadeVelha:
        idadeVelha = idade
        maisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media = somaidade/media
print('O Nome da pessoa mais velha é: {} e tem {} anos'.format(maisVelho, idadeVelha))
print('A media de idade do grupo é de: {} anos!'.format(media))
print('Existem {} mulheres com idade menores de 20 anos.'.format(totmulher20))
