print('===== SOMA DE NÚMEROS ======')
print('DIGITE 999 PARA PARAR O PROGRAMA')
cont = cont2 = n = 0
n = int(input('Digite um número:'))
while n != 999:
    cont += n
    cont2 += 1
    n = int(input('Digite um número:'))
print('Você digitou {} números e a soma deles foram de {}'.format(cont2, cont))
print('\033[0;31m~~~~~ PROGRAMA ENCERRADO ~~~~~')
