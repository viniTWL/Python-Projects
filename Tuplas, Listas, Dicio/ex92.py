from datetime import date
ano = date.today().year
dic = dict()
print('==== CARTEIRA DE TRABALHO ====')
while True:
    dic['nome'] = str(input('Nome:')).strip()
    data = int(input('Ano de Nascimento:'))
    dic['idade'] = ano - data
    dic['ctps'] = int(input('Carteira de Trabalho: (Se não possui, tecle 0)'))
    if dic['ctps'] == 0:
        print('''Nome: {}.
Idade: {}.
Não possui carteira de trabalho.'''.format(dic['nome'], dic['idade']))
        break
    else:
        dic['ano'] = int(input('Ano de Contratação:'))
        dic['sal'] = float(input('Salário:'))
    apos = (dic['ano'] + 35) - data #calculando ano de aposentadoria
    print('-'*35)
    print('''O nome do contribuinte é {}.
Tem {} anos.
Seu CTPS é {}.
Sua primeira contratação foi em {}.
Seu salário é de R${}.
Sua aposentadoria será com {} anos.'''.format(dic['nome'], dic['idade'], dic['ctps'], dic['ano'], dic['sal'], apos))
    break











