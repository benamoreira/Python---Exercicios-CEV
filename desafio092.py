from datetime import date
dados = dict()
dados['nome'] = str(input('Nome:'))
data = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - data
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = int(input('Salário: '))
    anostrabalhados = date.today().year - dados['contratação']
    dados['aposentadoria'] = 35 - anostrabalhados + dados['idade']
for k, v in dados.items():
    print(f'O {k} tem o valor {v}.')
