nome = ''
preço = totalcompra = contprecomaior = precoprodbarato = cont = 0
nomeprodbarato = ''
while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('RS: '))
    cont += 1
    totalcompra += preço
    if preço > 1000:
        contprecomaior += 1
    if cont == 1 or preço<precoprodbarato:
        precoprodbarato = preço
        nomeprodbarato = nome
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
print('RESUMO DE COMPRAS')
print(f'O Total gasto foi de RS{totalcompra:.2f}!')
print(f'{contprecomaior} produtos, custaram mais de R$1.000,00')
print(f'O produto mais barato foi {nomeprodbarato} que custa {precoprodbarato:.2f}!')