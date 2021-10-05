soma = 0
cont = 0
print('===== Digite 6 números inteiros, será somado apenas os pares =====')
for c in range(1, 7):
    num = int(input('Numero {}:'.format(c)))
    if num % 2 == 0:  #condição para definir os paraes
        soma = soma + num # somando os numeros pares
        cont = cont + 1 # contando quais são pares
print('resultado {}, a soma foi {}'.format(cont, soma))
