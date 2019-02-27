reta1 = int(input('Digite a reta 1: '))
reta2 = int(input('Digite a reta 2: '))
reta3 = int(input('Digite a reta 3: '))

if reta1 < reta2+reta3 and reta2 < reta1+reta3 and reta3 < reta1+reta2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO ', end='')

    if reta1== reta2 == reta3:
        print('EQUILATERO!')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PÓDEM FORMAR UM TRIÂNGULO')