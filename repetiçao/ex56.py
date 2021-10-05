soma = 0
homem = 0
idadehomem = 0
homemvelho = ''
mulher = 0
print('\033[1;34m===== ANALISADOR DE DADOS =====\033[m')
for i in range(1, 5):
    print('- PESSOA {}'.format(i))
    nome = str(input('Digite seu primeiro nome:'))
    idade = int(input('Digite sua idade:'))
    sexo = str(input('Digite seu sexo [M/F]:')).upper().strip()
    soma += idade
    if i == 1 and sexo == 'M':
        idadehomem = idade
        homemvelho = nome
    if sexo == 'M' and idade > idadehomem:
        idadehomem = idade
        homemvelho = nome
    if sexo == 'F' and idade < 20:
        mulher += 1
media = soma/4
print('A média é de {:.1f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(idadehomem, homemvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher))