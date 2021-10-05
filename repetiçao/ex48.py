soma = 0
cont = 0
for c in range(1, 501, 2):
    #print(c, end='-')
    if c % 3 == 0:
        cont += 1
        soma = soma + c
print('Os numeros sao {}, e soma {}'.format(cont, soma))

