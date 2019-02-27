n = c = prod = 0
while True:
    n = int(input('Digite um Nº: '))
    if n < 0:
        break
    print(f'A Tabuada de: {n} é : ')
    c = 0
    while c <= 10:
        prod = n * c
        print(f' {n}x{c} = {prod} ')
        c += 1
print('FIM!!!')