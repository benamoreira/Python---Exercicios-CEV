from datetime import date
anoNasc = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year

verificaIdade = anoAtual-anoNasc

if verificaIdade < 18:
    verificaIdade = 18-verificaIdade
    print('Voce ainda não precisa se alistar.')
    print('Faltam {} anos para voce comparecer!'.format(verificaIdade))

elif verificaIdade == 18:
    print('Voce precisa se alistar ainda este ano!')

else:
    verificaIdade = verificaIdade-18
    print('Você não precisa se alistar!')
    print('Já se passaram {} anos da data em que precisou!'.format(verificaIdade))
