str(print('Bem vindo ao nosso site de Viagens!'))
d = float(input('Qual será a distância em km que você irá percorrer?'))
if d <= 200:
    print('Essa viagem custará R${:.2f}, pois está abaixo de 200km'.format(float(d*0.50)))
else:
    print('Essa viagem custará R${:.2f}, pois está acima de 200km'.format(float(d*0.45)))





