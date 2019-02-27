valores = list()
maiorValor = menorValor = 0
for pos in range(0, 5):
    valores.append(int(input(f'Digite o valor na Posição {pos}: ')))
    if pos == 0:
        menorValor = valores[pos]
        maiorValor = valores[pos]
    else:
        if valores[pos] > maiorValor:
            maiorValor = valores[pos]
        if valores[pos] < menorValor:
            menorValor = valores[pos]
print('=-'*30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor é: {maiorValor} na posições: ',end='')
for i, v in enumerate(valores):
    if v == maiorValor:
        print(f'{i}...',end='')
print()
print(f'O menor Valor é: {menorValor} nas posicções: ',end='')
for i, v in enumerate(valores):
    if v == menorValor:
        print(f'{i}...',end='')
print()