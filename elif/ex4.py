from datetime import date #modulo de data
str(print('\033[1;32mBem-vindo ao nosso site para alistamento militar!'))
str(print('Digite seus dados...\033[m'))
nome = str(input('\033[4;30mDigite seu nome completo:')).strip()
pn = nome.split() #divindo o nome
ano = int(input('Digite o ano de seu nascimento:'))
atu = date.today().year
res = atu - ano
if res == 18:
    print('\033[0;92m{}, você já pode se alistar.'.format(pn[0]))
elif res <= 17:
    print('\033[0;92m{}, você ainda não precisa se alistar, faltam {} anos para seu alistamento.'.format(pn[0], 18-res))
    print('Seu alistamento será em {}.'.format((atu+18)-res))
elif res > 18:
    print('\033[0;92m{}, já se passou {} anos de seu período de alistamento.'.format(pn[0], res-18))
    print('Seu alismento foi em {}.'.format(atu-(res-18)))

#pn[0] é o primeiro nome

