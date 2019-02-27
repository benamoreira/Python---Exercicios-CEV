palavras = ('tudo', 'nada', 'estudar', 'carro', 'mercado', 'mesa', 'janela',
            'livro', 'computador', 'lapis', 'caneta', 'celular')


for pos in palavras:
    print(f'\nNa palavra {pos.upper()} temos as vogais: ', end='')
    for letra in pos:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
