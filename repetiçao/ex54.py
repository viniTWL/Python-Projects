from datetime import date
cont = 0
cont2 = 0
ano = date.today().year
print('\033[1;37m====== Verificando se é maior ou menor de idade ======\033[m')
for pessoas in range(1, 8):
    nasc = int(input('Pessoa {}. Digite seu ano de nascimento:'.format(pessoas)))
    if ano - nasc >= 18:
        cont += 1
    elif ano - nasc < 18:
        cont2 += 1
print('O número de pessoas maiores de idade foram {}, e o de menores de idade foram {}.'.format(cont, cont2))