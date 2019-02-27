matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somacoluna = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valores para [{l}/{c}]: '))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            somacoluna += matriz[l][2]
        if matriz[l][c] == matriz[2][c]:
            if c == 0:
                mai = matriz[1][c]
            elif matriz[1][c] > mai:
                mai = matriz[1][c]
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print('=-'*30)
print(f'A soma dos valores pares é: {somapares}')
print(f'A soma dos valores da 3ª coluna é: {somacoluna}')
print(f'O maior valore da segunda linha é: {mai}')