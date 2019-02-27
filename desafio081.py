numeros = list()
opc = ''
while True:
    numeros.append(int(input('Digite um valor: ')))
    opc = str(input('Quer continuar? [S/N]')).upper()[0]
    numeros.sort(reverse=True)
    if opc in 'nN':
        break
print('-='*30)
print(f'Foram digitados {len(numeros)} números!')
print(numeros)
if 5 in numeros:
    print(f'O nº5 foidigitado na {numeros.index(5)} posição.')
else:
    print ('O número 5 não foi digitado.')