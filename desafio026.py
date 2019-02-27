frase = str(input('Digite uma Frase: ')).strip()
print('Aparecem {} vezes a letra A nesta frase'.format(frase.upper().count('A')))
print('A primeira vez que a plavra  A aparece é no {} carcatere'.format(frase.lower().find('a')+1))
print('A primeira vez que a plavra  A aparece é no {} carcatere'.format(frase.lower().rfind('a')+1))