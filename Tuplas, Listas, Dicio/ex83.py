ex = str(input('Digite sua expressão:'))
lista = list(ex)
e = lista.count('(')
d = lista.count(')')
r = e + d
if r % 2 == 0:
    print('\033[0;32mSua expressão está válida!')
else:
    print('\033[0;31mSua expressão está inválida!')