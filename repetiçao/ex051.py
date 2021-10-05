pt = int(input('Digite o primeiro termo de sua P.A:'))
r = int(input('Digite a razão da sua P.A:'))
termo = pt
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += r
    cont += 1
print('fim')