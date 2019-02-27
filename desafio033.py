n1 = int(input('Digite o 1º nº: '))
n2 = int(input('Digite o 2º nº: '))
n3 = int(input('Digite o 3º nº: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('Menor valor: {}'.format(menor))
print('Maior valor: {}'.format(maior))