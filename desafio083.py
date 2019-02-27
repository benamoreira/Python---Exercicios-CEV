expressão =str(input('Digite Sua expressão: '))
pilha = list()

for símb in expressão:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append()
            break
if len(pilha) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão é invalida!')
