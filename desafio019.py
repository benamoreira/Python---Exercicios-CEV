from random import  choice
alunoa = str(input('Digite o nome do Aluno 1:'))
alunob = str(input('Digite o nome do Aluno 2:'))
alunoc = str(input('Digite o nome do Aluno 3:'))
alunod = str(input('Digite o nome do Aluno 4:'))
lista = [alunoa, alunob, alunoc, alunod]
alunoSelec = choice(lista)
print('O aluno que apaga a lousa é: {}'.format(alunoSelec))