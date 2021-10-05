d = float(input('Informe por quantos dias o carro foi alugado:'))
km = float(input('Informe quantos quilômetros foram percorridos:'))
pd = d*60
pkm = km*0.15
print('De acordo com os dias alugados e a quilometragem percorrida, você terá de pagar o total de R${:.2f} pelo aluguel do carro.'.format(pd+pkm))

