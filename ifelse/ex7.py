s = float(input('Digite o valor do seu salário:'))
if s >= 1250.00:
    print('O seu salário aumentou em 10% pois está superior a R$1250.00, portanto agora voce recebe R${}.'.format(s+(s * 10 / 100)))
else:
    print('O seu salário aumentou em 15% pois é inferior a R$1250.00, agora você recebe R${}.'.format(s+(s * 15 / 100)))
    #a formula variavel * x/100 , significa porcentagem, no exercicio x=10,15



