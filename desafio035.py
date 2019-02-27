r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima, PODEM FORMAR TRIANGULO!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR TRIANGULO!')