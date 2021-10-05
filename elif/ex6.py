from datetime import date
str(print('\033[0;34mBem-vindo ao site da Confederação Nacional de Natação!'))
str(print('\033[0;37mVamos definir sua categoria de acordo com seus dados...'))
nome = input('Digite seu nome:')
pn = nome.split()
ano = int(input('Digite o ano de seu nascimento:'))
atu = date.today().year
res = atu - ano
print('\033[0;37mDe acordo com seus dados...')
if res <= 9:
    print('{},você tem {} anos e pertence a categoria \033[0;32mMirim.'.format(pn[0], res))
elif res <= 14:
    print('{},você tem {} anos e pertence a categoria \033[0;32mInfantil.'.format(pn[0], res))
elif res <= 19:
    print('{},você tem {} anos e pertence a categoria \033[0;32mJunior.'.format(pn[0], res))
elif res <= 20:
    print('{},você tem {} anos e pertence a categoria \033[0;32mMaster.'.format(pn[0], res))
elif res > 20:
    print('{},você tem {} anos e pertence a categoria \033[0;36mSenior.'.format(pn[0], res))
