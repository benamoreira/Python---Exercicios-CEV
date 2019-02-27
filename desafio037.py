num = int(input('Digite um Nº: '))
print('Digite a opção de Base para conversão: ')
print('1 - Binário;  2 - octal; 3 - hexadecimal')
opção = int(input('Opc: '))

if opção == 1:
    binario = bin(num)
    print('O valor em binário é: {}'.format(binario))

elif opção == 2:
    octa = oct(num)
    print('O valor octal é: {}'.format(octa))

elif opção == 3:
    hexa = hex(num)
    print('O valor para hexadecimal é: {}'.format(hexa))

else:
    print('Opção invalida!')

print('Obrigado!')