soma = 0 #somatorio
cont = 0 #contador
print('Digite números pares para fazer a soma deles, ímpares serão desconsiderados.')
for c in range(1, 7):
    n = int(input('Digite o valor {}:'.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Você informou {} números pares, e a soma deles foi {}.'.format(cont, soma))


