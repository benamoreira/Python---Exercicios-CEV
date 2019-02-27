print('Gerador de PA')
print('-=' *10)

primeiro = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
print('A PA de {} com razão {} :'.format(primeiro, razao))
c=1
maistermos = 10
total = 0

while maistermos!= 0:
    total = total+maistermos
    while c <= total:
        termo = termo + razao
        c = c+1
        print('{} - '.format(termo), end='')
    maistermos = int(input('Quantos termos a mais você deseja? '))

print('Voce saiu do programa!!!')
print('Foram apresentados no {} no total.'.format(total))