menu = 0
n1 = int(input('Digite um nº: '))
n2 = int(input('Digite outro nº: '))

while menu != 5:
    print('------ MENU ------')
    menu = int(input('''[1] - Somar
[2] - Multiplicar
[3] - maior
[4] - Novos    Numeros
[5] - Sair
OPC: '''))

    if menu == 1:
        resultado = n1+n2
        print('A soma é: {}'.format(resultado))

    elif menu == 2:
        resultado = n1*n2
        print('A multiplicação entre eles equivale á: {}'.format(resultado))

    elif menu == 3:
        if n1>n2:
            resultado = n1
            print('O maior é: {}'.format(resultado))
        else:
            resultado = n2
            print('O maior é: {}'.format(resultado))

    elif menu ==4:
        print('Digite os números novamente:')
        n1 = int(input('1º Valor: '))
        n2 = int(input('2º Valor: '))

    elif menu == 5:
        print('Finalizando ...')

    else:
        print('Opção Invalida!. Tente Novamente.')

print('FIM. Voce Fechou o programa!')