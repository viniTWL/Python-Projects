from random import randint
print('=-'*13)
print(' VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*13)
cont = 0
while True:
    n = int(input('Digite seu número:'))
    pi = str(input('Par ou ímpar?[P/I]')).strip().upper()
    while pi not in 'PI':
        pi = str(input('Par ou ímpar?[P/I]')).strip().upper()
    comp = randint(0, 10)
    r = n + comp
    print(f'Você jogou {n} e o computador jogou {comp}. O resultado é {r}')
    if pi == 'P' and r % 2 == 0:
        print('É par! Você ganhou!')
        cont += 1
    elif pi == 'I' and r % 2 == 0:
        print('É par! Você perdeu!')
        print('GAME OVER! Você venceu {} vezes!'.format(cont))
        break
    elif pi == 'P' and r % 2 == 1:
        print('É impar! Você perdeu!')
        print('GAME OVER! Você venceu {} vezes!'.format(cont))
        break
    elif pi == 'I' and r % 2 == 1:
        print('É impar! Você ganhou!')
        cont += 1
