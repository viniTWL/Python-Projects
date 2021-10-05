maior = 0
menor = 9999999999
print('Verificando o maior e menor peso de 5 pessoas')
for c in range(1, 6):
    peso = float(input('Digite o peso da {}a pessoa:'.format(c)))
    if peso == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi o de {}Kg.'.format(maior))
print('E o menor peso lido foi o de {}Kg.'.format(menor))
