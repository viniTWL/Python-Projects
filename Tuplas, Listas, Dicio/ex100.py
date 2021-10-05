from random import choice
from time import sleep
numeros = list()
pares = list()
nums = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
def sorteia():
    print('Sorteando os valores da lista:', end='')
    for i in range(0, 5):
        sorts = choice(nums)
        numeros.append(sorts)
        print(sorts, end=' ', flush=True)
        sleep(0.5)
def soma():
    for c in numeros:
        if c % 2 == 0:
            pares.append(c)
    r = sum(pares)
    print(f'Somando os valores pares sorteados de {numeros}, temos como resultado: {r}')
#PROGRAMA
sorteia()
print()
soma()
