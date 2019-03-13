pessoa = dict()
listapessoas = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F !')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    listapessoas.append(pessoa.copy())
    opc = str(input('Quer continuar [S/N]')).upper()
    if opc in 'nN':
        break
print('-='*29)
print(listapessoas)
print('-='*29)
print(f'A - O grupo tem {len(listapessoas)}')
media = soma /len(listapessoas)
print(f'B - A média de idade é de {media}')
print('As mulheres cadastradas foram ', end='')
for p in listapessoas:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]} ',  end='')
print()
print('D - Lista das pessoas que estão acima da média: ')
for p in listapessoas:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRADO!!!')

