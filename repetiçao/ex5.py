soma = 0
cont = 0
print('\033[0;32mA soma entre todos os numeros que são multiplos de 3 de 0 a 500\033[m')
for c in range(1, 501, 2): #mostrando somento os numeros impares
    if c % 3 == 0: #apenas numeros divisiveis por 3, logo multiplos de 3
        cont = cont + 1
        soma = soma + c
print('Foram solicitados {} números, e a soma dos números é {}.'.format(cont, soma))




