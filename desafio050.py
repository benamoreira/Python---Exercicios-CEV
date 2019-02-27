s=0
for c in range (0,4):
    num = int(input('Digite um valor: '))
    if num %2 == 0:
        s+=num
print('A soma final é de: {}'.format(s))
