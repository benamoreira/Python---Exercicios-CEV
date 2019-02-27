idade = maior18 = cont18 = contHom = contMul20 = 0
sexo = ''
opcrepete = ''
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    opcrepete = str(input('Desejar continuar? [S/N]: ')).upper().strip()[0]
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        contHom += 1
    if sexo == 'F' and idade < 20:
        contMul20 += 1
    if opcrepete == 'N':
        break
print(f'Você digitou {cont18} pessoas com mais de 18 anos;')
print(f'Foram cadastrados {contHom} Homens.')
print(f'Existem {contMul20} mulheres com menos de 20 anos!')