alt = float(input('Qual a altura?'))
larg = float(input('Qual a largura?'))
area = alt*larg
tinta = area//2
print('A altura: {}. Largura:{}'.format(alt,larg))
print('A area é de :', area)
print('São necessários {}latas de tinta para pintar esta parede.'.format(tinta))