from time import sleep
print('\033[1;35m ====== 10 TERMOS DE UMA P.A ====== \033[m')
pt = int(input('Digite o primeiro termo de sua P.A:'))
r = int(input('Digite a razão de sua P.A:'))
for c in range(pt, pt + (11 - 1) * r, r):
    print(c, end=' - ')
print('Esse foi o resultado da P.A que começou em \033[0;35m{} \033[mcom razão \033[0;35m{}\033[m.'.format(pt, r))
