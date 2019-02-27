from random import randint
num = randint(0,5)
chute = int(input('Digite um nº de 0 a 5: '))
print('O nº gerado foi: {}'.format(num))
if num == chute:
    print('Se é o bixão mesmo, heim doido!')
else:
    print('kkk se liga!')
