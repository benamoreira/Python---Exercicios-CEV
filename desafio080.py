valores = list()
for i in range(0, 5):
    num = int(input('Digite o nº: '))
    if i == 0 or num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num < valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1
print('=-'*30)
print(valores)

