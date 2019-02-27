soma = n = c = 0

while n != 999:
    n = int(input('Digite um nº: '))
    if n != 999:
        soma = soma + n
        c = c+1

print('Voce digitou {} numeros e o soma de todos eles equivalem a: {}'.format(c, soma))