lista = list()
listapar = list()
listaimpar = list()

while True:
    lista.append(int(input('Digite um nº: ')))
    opc = str(input('Deseja Continuar? [S/N]: '))
    if opc in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    elif v % 2 == 1:
        listaimpar.append(v)

print(f'A Lista completa é: {lista}')
print(f'A lista de pares é: {listapar}')
print(f'A lista de ímpares é: {listaimpar}')