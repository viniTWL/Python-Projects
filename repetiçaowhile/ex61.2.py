print('===== P.A USANDO O "FOR" =====')
pt = int(input('Digite o primeiro termo de sua P.A:'))
r = int(input('Digite a razão da sua P.A:'))
cont = 1
for c in range(pt, pt + (11 - 1) * r, r):
   print(c, end=' > ')
print('Fim.')


