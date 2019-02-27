maiorPeso = 0
menorPeso = 0

for p in range(1,6):
    peso = float(input('Digite o peso da {}ª Pessoa: '.format(p)))
    if p==1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso>maiorPeso:
            maiorPeso =peso
        if peso<menorPeso:
            menorPeso = peso

print('O Maior peso foi: {}'.format(maiorPeso))
print('O menor peso foi: {}'.format(menorPeso))