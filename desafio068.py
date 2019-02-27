from random import randint
opc = ''
n = nPc = soma = contavitoria = 0
while True:
    opc = str(input('Escolha Par ou Impar [P/I]: ')).strip().upper()[0]
    n = int(input('Escolha de 1 a 5: '))
    nPc = randint(1,5)
    soma = n +nPc
    if soma % 2 == 0:
        print('PAR')
        if opc == 'P':
            print(f'A soma deu {soma}! Você ganhou!!!')
        else:
            print(f'A soma deu {soma}! Você perdeu!!!')
            break
    if soma % 2 == 1:
        print('IMPAR')
        if opc == 'I':
            print(f'A soma deu {soma}! Você ganhou!!!')
        else:
            print(f'A soma deu {soma}! Você perdeu!!!')
            break
    contavitoria += 1
print(f'Você ganhou {contavitoria} vezes até ser derrotado!')