velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Voçe foi Multado!')
    valorMulta = (velocidade -80)*7
    print('O valor da multa é de R${}!'.format(valorMulta))
else:
    print('Suave!')