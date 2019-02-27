pessoas = list()
pessoa = list()
mai = men = 0
while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        if pessoa[1] < men:
            men = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    opc = str(input('Deseja continuar? [S/N]: ')).upper()
    if opc in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas!')
print(f'O maior peso foi de {mai} Kg. Peso de ')
for p in pessoas:
    if p[1] == mai:
        print(f'{[p[0]]}')
print(f'O menor peso foi de {men} Kg')
for p  in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]')