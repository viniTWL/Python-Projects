from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(40 * '=')
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}.')
    if inicio > fim:
        passo *= -1
        fim -= 1
    else:
        fim += 1
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.5)
    print()
#PROGRAMA
contador(1, 10, abs(1))
contador(10, 0, abs(-2))
print(40 * '=')
print('Agora é a sua vez de personalizar a contagem!')
a = int(input('INÍCIO: '))
b = int(input('FIM: '))
d = int(input('PASSO: '))
contador(a, b, abs(d))
