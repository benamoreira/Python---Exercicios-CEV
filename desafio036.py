valorCasa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o seu salário? '))
qtdeanos = int(input('Em quantos anos pretende? '))

meses = qtdeanos*12
limiteSalario = salario*0.30
print(meses)

if valorCasa/meses < limiteSalario:
    print('Emprestimo será aprovado no valor de R${:.2f}'.format(valorCasa/meses))

else:
    print('Infelizmente voce não poderá financiar esta casa!')

