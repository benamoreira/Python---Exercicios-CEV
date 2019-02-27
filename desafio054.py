from datetime import date

contMaior = 0
contMenor = 0

anoAtual = date.today().year

for c in range(1,8):
    idade = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idadeAtual = anoAtual-idade
    if 0 < idadeAtual < 21:
        contMenor += 1
    else:
        contMaior += 1
print('{} pessoas, ainda são menores de idade!'.format(contMenor))
print('E outras {} pessoas, já são maiores de idade!'.format(contMaior))