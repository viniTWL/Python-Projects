from datetime import date #peguei a data atual
ano = int(input('Digite um ano qualquer:'))
if ano == 0:
    ano = date.today().year #comando para colocar o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #bissexto precisa ser dividido por 4, multiplo de 100 e de 400
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))
