nomeCompleto = str(input('Digite um nome completo: ')).strip()
nomeDividido = nomeCompleto.split()
print('O primeiro nome é {}'.format(nomeDividido[0]))
print('O ultimo nome é {}'.format(nomeDividido[len(nomeDividido)-1]))
