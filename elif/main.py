str(print('\033[0;34mBem-vindo ao site de empréstimo bancário!\033[m'))
valor = float(input('Qual será o valor da casa desejada?R$'))
sal = float(input('Qual é a sua remenuração mensal?R$'))
ano = int(input('Em quantos anos você pretende pagar o imóvel?'))
a = ano * 12 #1 ano = 12 meses
pres = valor/a #prestação é o valor da casa dividido pelo número de meses
if pres > sal*0.3: #prestação menor que 30% do salario
    print('\033[0;31mA prestação é de R${:.2f} e está excendendo 30% de sua remuneração mensal,o empréstimo foi negado.'.format(pres))
else:
    print('\033[0;32mA prestação é de R${:.2f}.'.format(pres))


