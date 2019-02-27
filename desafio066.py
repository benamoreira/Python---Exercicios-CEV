n = cont = soma = 0
while True:
    n = int(input('Digite um Nº: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} números e a soma deles é: {soma}')