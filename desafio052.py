num = int(input('Digite um nº: '))
tot = 0
for c in range(1, num +1):
    if num % c ==0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\033[m - O nº {} foi divisivel {} vezzes!'.format(num, tot))
if tot ==2:
    print('E por isso é PRIMO!')
else:
    print('Por isso ele não é primo!!')