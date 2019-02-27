termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0

print('Os 10 primeiros termos do nº {} com razão {} são: '.format(termo, razao, end=''))
while c < 10:
    termo = termo + razao
    c = c+1
    print('{} , '.format(termo), end='')