def aumentar(num, x, formato=True):
    r = num * x
    res = num + r
    return res if formato == False else valor(res)


def diminuir(num, x, formato=True):
    r = num * x
    res = num - r
    return res if formato == False else valor(res)


def dobro(num, formato=True):
    res = num * 2
    return res if formato == False else valor(res)


def metade(num, formato=True):
    res = num / 2
    return res if formato == False else valor(res)


def valor(num=0, mon='R$'):
    return f'{mon}{num:.2f}'.replace('.', ',')


def resumo(num):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{valor(num)}')
    print(f'Dobro do preço: \t{dobro(num):}')
    print(f'Metade do preço: \t{metade(num):}')
    print(f'80% do aumento: \t{aumentar(num,0.8)}')
    print(f'35% de redução: \t{diminuir(num,0.35)}')
    print('-' * 30)