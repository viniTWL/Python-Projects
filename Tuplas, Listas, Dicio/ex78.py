lista = []
mai = 0
men = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {c}:')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print('-='*30)
print(f'Você digitou os números {lista}.')
print(f'O maior número digitado foi {mai} na posição', end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f' {i}...', end='')
print()
print(f'O menor número digitado foi {men} na posição', end='')
for i, v in enumerate(lista):
    if v == men:
        print(f' {i}...', end='')
