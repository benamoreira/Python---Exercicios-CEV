listanumerica = [[], []]
valor = 0
for p in range(0, 7):
    valor = int(input(f'Digite o {p+1}º valor:'))
    if valor % 2 == 0:
        listanumerica[0].append(valor)
    else:
        listanumerica[1].append(valor)
print('=-'*30)
listanumerica[0].sort()
listanumerica[1].sort()
print(f'Os valores pares digitados foram: {listanumerica[0]}')
print(f'Os valores impares foram: {listanumerica[1]}')