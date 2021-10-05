print('====== BANCO TWL ======')
v = int(input('Qual valor você quer sacar:\033[0;32mR$\033[m'))
tot = v
ced = 50
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if tot == 0:
            break
print('=-'*35)
print('====== Volte sempre ao BANCO TWL! ======')
print('\033[1;37mFICA COM DEUS PRA TODOS!')

