n1 = int(input('Digite a Nota 1: '))
n2 = int(input('Digite a Nota 2: '))
mediaNotas = (n1+n2)/2

print('A NF foi: {}!'.format(mediaNotas))

if mediaNotas < 5.0:
    print('REPROVADO!')

elif mediaNotas >= 5.0 and mediaNotas < 6.9:
    print('RECUPERAÇÃO')

else:
    print('APROVADO!')