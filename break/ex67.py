print('\033[1;36m===== TABUADA =====\033[m')
while True:
    print('~~~~~ Número negativo encerra o programa ~~~~~')
    n = int(input('Digite um número para ver a sua tabuada:'))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
print('\033[1;31m====== PROGRAMA TABUADA ENCERRADO =====')

