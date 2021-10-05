tot = pro = bar = 0
nbar = '' #nome produto mais barato
print('\033[1;35m====== TWL STORE ======\033[m')
while True:
    n = str(input('Qual produto você deseja?')).strip()
    p = float(input('Qual o preço desse produto?\033[0;32mR$\033[m'))
    bar = p
    nbar = n
    if p < bar:
        bar = p
        nbar = n
    tot += p
    if p >= 1000:
        pro += 1
    r = str(input('Quer continuar suas compras?[S/N]')).strip().upper()
    while r not in 'SN':
        r = str(input('Quer continuar suas compras?[S/N]')).strip().upper()
    if r == 'S':
        print('\033[0;35m>>> PRÓXIMO PRODUTO <<<\033[m')
    elif r == 'N':
        break
print('-'*35)
print(f'O total da compra foi R${tot}')
print(f'{pro} produtos custaram mais de R$1000.00.')
print(f'O produto mais barato foi {nbar} e custou R${bar}.')
print('\033[1;35m===== VOLTE SEMPRE! =====')

