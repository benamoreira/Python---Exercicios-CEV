print('='*20)
print('PROGRESSÃO ARITIMETCA')
print('='*20)

primeiro = int(input('Primeiro termo:'))
razao = int(input('Digite a razão:'))

decimo = primeiro + (10-1)* razao

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU!')