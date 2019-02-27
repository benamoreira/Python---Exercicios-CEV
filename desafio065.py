continua = ''
maior = menor = media = soma = c = n = 0

print('-'*30)
print('DESAFIO 065')
print('-'*30)

while continua != 'N':
    n = int(input('Digite um nº: '))
    c += 1
    soma = soma + n


    if c ==1:
        maior =menor =n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    continua = str(input('Continuar? [S/N]')).upper().strip()[0]

media = soma/c
print('A média foi de {:.2f}. O maior valor foi : {} e o menor {}.'.format(media, maior, menor))