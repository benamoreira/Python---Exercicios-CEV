from random import randint
print('MEGA SENA')
lista = list()
jogos = list()
cont = 0
tot = 1
quant = int(input('QUantos jogos voce quer sortear? '))
while tot <= quant:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
    print(f'Os números sorteados foram: {jogos}')



