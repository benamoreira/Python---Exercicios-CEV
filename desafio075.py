n1 = int(input('Digite o 1º nº: '))
n2 = int(input('Digite o 2º nº: '))
n3 = int(input('Digite o 3º nº: '))
n4 = int(input('Digite o 4º nº: '))
numeros = (n1, n2, n3, n4)
print(f'Você digitou os valores : {numeros}')
print(f'O valor 9 apareceu: {numeros.count(9)} vezes!')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}')
else:
    print('O valor 3 não foi digitado!')

print(f'Os valores pares digitados foram: ', end='')
for n in numeros:
    if n%2 == 0:
        print(n, end='')
