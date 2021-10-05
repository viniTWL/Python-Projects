print('===== RESULTADOS DOS VALORES =====')
c = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while c == 'S':
    n = int(input('Digite um número:'))
    soma += n #soma
    cont += 1 #numero de valores digitados
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = str(input('Deseja continuar?[S/N]')).strip().upper()
print('A soma dos valores foi {} e a média foi {}.'.format(soma, soma/cont))
print('O menor número digitado foi {} e o maior foi {}.'.format(menor, maior))

