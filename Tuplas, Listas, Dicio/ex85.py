lista = [[], []]
num = 0
for i in range(1, 8):
    num = (int(input(f'Digite o nº{i}:')))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Os números ímpares foram {sorted(lista[0])}.')
print(f'Os números pares foram {sorted(lista[1])}.')
