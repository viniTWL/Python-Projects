from math import sin, cos, tan, radians
x = int(input('Digite o valor do ângulo:'))
s = sin(radians(x))
c = cos(radians(x))
t = tan(radians(x))
print('Seno:{:.2f}.'.format(s))
print('Cosseno:{:.2f}'.format(c))
print('Tangente:{:.2f}'.format(t))