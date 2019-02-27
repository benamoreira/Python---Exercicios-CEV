valores = list()
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor já na lista, digite outro nº!')
    else:
        valores.append(num)
        print('Valor adcionado a lista!')
    opc = str(input('Deseja continuar?[S/N]: ')).upper()
    if opc in 'Nn':
        break
print(valores)
valores.sort()
print (valores)