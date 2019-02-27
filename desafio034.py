salario = float(input('Digite o valor do Salario: '))
if salario > 1250:
    salarioNovo = salario*1.10
    print('Novo salario: R${:.2f}!'.format(salarioNovo))
else:
    salarioNovo = salario*1.15
    print('Novo Salario: R${:.2f}!'.format(salarioNovo))
