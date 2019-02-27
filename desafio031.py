distancia = int(input('Digite a distancia da Viaem em KM: '))
if distancia <= 200:
    distancia = distancia*0.50
    print('O valor da passagem é de R${:.2f}!'.format(distancia))
else:
    distancia = distancia*0.45
    print('O valor da passagem é de: R${}!'.format(distancia))
