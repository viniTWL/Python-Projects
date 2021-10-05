lista1 = []
lista2 = []
lista3 = []
lista4 = [lista1, lista2, lista3]
par = []
for i in range(1, 4):
    n = int(input(f'Digite um valor para a posição [0,{i}]:'))
    lista1.append(n)
    if n % 2 == 0:
        par.append(n)
for i in range(1, 4):
    n = int(input(f'Digite um valor para a posição [1,{i}]:'))
    lista2.append(n)
    if n % 2 == 0:
        par.append(n)
for i in range(1, 4):
    n = int(input(f'Digite um valor para a posição [2,{i}]:'))
    lista3.append(n)
    if n % 2 == 0:
        par.append(n)
print('=-'*30)
print(f'[  {lista1[0]}  ] [  {lista1[1]}  ] [  {lista1[2]}  ]')
print(f'[  {lista2[0]}  ] [  {lista2[1]}  ] [  {lista2[2]}  ]')
print(f'[  {lista3[0]}  ] [  {lista3[1]}  ] [  {lista3[2]}  ]')
print('=-'*30)
print(f'A soma dos pares é {sum(par)}.')
print(f'A soma dos valores ta terceira coluna é {lista1[2] + lista2[2] + lista3[2]}.')
print(f'O maior valor da segunda linha é {max(lista2)}.')

