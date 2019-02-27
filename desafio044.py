preçoNormal = float(input('Digite o preço do produto: '))
print(''' FORMAS DE PAGAMENTO
[1] A vista Deinheiro/Cheque
[2] Á vista no cartão
[3] 2x no Cartão
[4] 3x ou Mais no cartão
''')
opcPag = int(input('Qual a forma de Pagamento?: '))

if opcPag == 1:
    valorFinal = preçoNormal * 0.90
    print('O valor fica em R${:.2f}.'.format(valorFinal))
elif opcPag == 2:
    valorFinal = preçoNormal *0.95
    print('O valor a vista no cartão fica em R$ {}'.format(valorFinal))
elif opcPag == 3:
    valorFinal = preçoNormal
    parcela = preçoNormal/2
    print('Sua compra foi parcelada em 2x de : R${:.2f}'.format(parcela))
elif opcPag == 4:
    valorFinal = preçoNormal * 1.20

print('Sua ompra de R${:.2f} vai custar R${:.2f} no final.'.format(preçoNormal, valorFinal))