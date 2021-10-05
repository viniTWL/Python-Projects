lista = list()
dic = dict()
agelist = list()
wlist = list()
cont = idade = 0
while True:
    cont += 1
    dic['nome'] = str(input('Digite o primeiro nome:')).strip()
    sexo = str(input('Digite o sexo[M/F]:')).strip().upper()
    while True:
        if sexo not in 'MF':
            sexo = str(input('Digite o sexo[M/F]:')).strip().upper()
        if sexo in 'MF':
            dic['sexo'] = sexo
            break
    dic['idade'] = (int(input('Digite a idade:')))
    idade += dic['idade']
    lista.append(dic.copy())
    dic.clear()
    r = str(input('Quer continuar?[S/N]'))
    if r in 'Ss':
        print('-'*30)
    elif r in 'Nn':
        print('\033[0;31m ---- PROGRAMA FINALIZADO -----\033[m')
        break
media = idade/cont
print(f'- Foram cadastradas {cont} pessoas.')
print(f'- A média de idade foi {media}.')
print('- A lista de mulheres cadastradas foi', end='')
for i in lista:
    if i['sexo'] == 'F':
        print(i['nome'], end='')
print()
print('- Lista de pessoas que estão acima da média de idade:')
for p in lista:
    if p['idade'] > media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('----------------- ACABOU -------------------')

