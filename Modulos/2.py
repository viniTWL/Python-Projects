from math import hypot
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
r = hypot(co,ca)
print('O comprimento da hipotenusa será {:.2f}'.format(r))

