contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um Nº entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ',end='')
print(f'O nº {n}, por extenso é: {contagem[n]}!')