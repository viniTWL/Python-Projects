
Victor Silva
há 1 ano
Mano todos os exercícios eu fiz com o dobro de linhas do Guaná, só esperando o dia que eu conseguiria fazer um com menos linhas. E esse dia chegouuuu crlll q orgulho man.. To ligado que isso não quer dizer nada, mas to feliz mesmo assim kkk

from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    for c in range(inicio, fim+1, passo):
        print(c, end = ' ')
        sleep(0.5)
    print()




contador(1,10,0)
contador(10,0,2)
contador(int(input('Digite o ínicio: ')), int(input('Ditite o fim: ')), int(input('Digite o passo: ')))