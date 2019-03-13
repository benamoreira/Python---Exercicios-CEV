dadosAluno = dict()
dadosAluno['nome'] = str(input('Digite o nome: '))
dadosAluno['média'] = float(input(f'Digite a média do Aluno {dadosAluno["nome"]}: '))
if dadosAluno['média'] >= 7:
    dadosAluno['situação'] = 'Aprovado'
elif 5 <= dadosAluno['média'] < 7:
    dadosAluno['situação'] = 'Recuperação'
else:
    dadosAluno['Situação'] = 'Reprovado'
for k, v in dadosAluno.items():
    print(f'O {k} é igual a {v}')