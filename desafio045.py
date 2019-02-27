import random
from time import sleep
itens = ('Pedra','Papel','Tesoura')
opcPc = random.randint(0,2)
opcuser = int(input('''DIGITE A OPÇÃO
[0] Pedra
[1] Papel
[2] Tesoura
OPC: '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*15)
print('O computador jogou: {}'.format(itens[opcPc]))
print('O jogador jogou: {}'.format(itens[opcuser]))
print('-='*15)

if opcPc == 0:
    if opcuser == 0:
        print('EMPATE')
    elif opcuser == 1:
        print('Jogador VENCE!')
    elif opcuser == 2:
        print('Computador Vence!')
    else:
        print('Jogada Invalida!')

elif opcPc == 1:
    if opcuser == 0:
        print('Computadro Vence')
    elif opcuser == 1:
        print('Empate!')
    elif opcuser == 2:
        print('Jogador Vence')
    else:
        print('Jogada INvalida!')

elif opcPc == 2:
    if opcuser == 0:
        print('jogador VENCE')
    elif opcuser == 1:
        print('Computador Vence!')
    elif opcuser == 2:
        print('EMPATE!')
    else:
        print('Jogada INvalida!')
