v = float(input('Velocidade do veículo na via:'))
if v >= 80:
    print('Você estava acima da velocidade permitida, sua multa será de: R${:.2f}.'.format(v*7-560)) #velocidade vezes a multa - 80*7=560
else:
    print('Você estava na velocidade permitida, continue assim!')
