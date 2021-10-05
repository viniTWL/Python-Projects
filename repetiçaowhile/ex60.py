from time import sleep
n = int(input('Digite um número para ver o seu fatorial:'))
c = n
f = 1
while c > 0:
    print('{}'.format(c,), end='')
    print(' x ' if c > 1 else ' = ', end='' ) #colocando o = depois do 1
    f *= c #multiplicando os numeros
    c -= 1 #contando os números
print('\033[0;32mCALCULANDO...\033[m', end='\n')
sleep(3)
print('\nO fatorial de \033[0;32m{}\033[m é \033[0;32m{}.'.format(n, f))


