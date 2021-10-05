from time import sleep
def factorial(num, show=True):
    """num = numero escolhido pelo usuario
    show True: Mostra os numeros fatorados
    show False: Não mostra"""
    f = 1
    if show == True:
        for i in range(num, 0, -1):
            f *= i
            print(i, end='')
            print(' x ' if i > 1 else ' = ', end='')
        sleep(2)
        print(f)
    if show == False:
        for i in range(num, 0, -1):
            f *= i
        sleep(2)
        print(f)

#help(fatorial)

#Programa
n = int(input('Digite o número para ver seu fatorial:'))
s = str(input('Deseja mostrar os números a serem fatorados?[S/N]'))
if s in 'Ss':
    factorial(n, show=True)
if s in 'nN':
    print('Resultado:', end='')
    factorial(n, show=False)
