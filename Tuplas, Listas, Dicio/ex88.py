from random import sample
from time import sleep
lista = []
print('\033[0;34m-'*30)
print('     \033[0;34mJOGOS DA MEGA SENA')
print('\033[0;34m-\033[m'*30)
j = int(input('Quantos jogos você deseja gerar? '))
print('SORTEANDO...')
for i in range(0, j):
    ran = sorted(sample(range(1, 60), 6))
    lista.append(ran[:])
    sleep(2)
    print(f'Jogo {i+1}:{lista[i]}')
