def area(b, a):
    r = b * a
    print(f'O tamanho da área é {r}')

while True:
    b = float(input('Digite a largura:'))
    a = float(input('Digite o comprimento:'))
    area(b, a)
    res = str(input('Continuar com os cálculos?[S/N]')).strip().upper()
    if res == 'S':
        print('-'*30)
    elif res == 'N':
        break
    while res not in 'NS':
        res = str(input('Continuar com os cálculos?[S/N]')).strip().upper()
        if res == 'S':
            print('-' * 30)
        elif res == 'N':
            break
print('\033[0;31m===== PROGRAMA FINALIZADO =====')
