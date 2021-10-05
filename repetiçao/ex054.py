cont1 = 0
cont2 = 0
from datetime import date
atual = date.today().year
for i in range(1, 8):
    ano = int(input('Pessoa {} - Digite seu ano de nascimento:'.format(i)))
    if atual - ano >= 18:
        cont1 += 1
    elif atual - ano < 18:
        cont2 += 1
print('{} pessoas já são maiores de idade, {} ainda não são.'.format(cont1, cont2))





