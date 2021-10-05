#CALCULANDO MÉDIA
n1 = float(input('Digite sua nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1+n2)/2 # calculo basico de media
print('Sua média foi de {:.2f}.'.format(m))
if m >= 6: # se o valor da media igual a 6 ou maior
    print('Sua média está boa!')
else:
    print('Sua média não está boa!')
