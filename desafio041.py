from datetime import date
anoNasc = int(input('Digite o ano de Nascimento do Atleta: '))
anoAtual = date.today().year

idadeAtleta = anoAtual-anoNasc

if idadeAtleta <= 9:
    print('Atleta MIRIM!')
elif idadeAtleta > 9 and idadeAtleta <= 14:
    print('Infantil!')
elif idadeAtleta>14 and idadeAtleta<=19:
    print('JUNIOR')
elif idadeAtleta > 19 and idadeAtleta <= 20:
    print('SÊNIOR!')
else:
    print('MASTER!')

