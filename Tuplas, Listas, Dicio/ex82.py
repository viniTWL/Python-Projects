lista = []
parlista = []
imlista = []
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    if n % 2 == 0:
        parlista.append(n)
    else:
        imlista.append(n)
    r = str(input('Deseja continuar?[S/N]')).strip()
    if r in 'Ss':
        print('=-'*35)
    elif r in 'nN':
        break
    else:
        print('OPÇÃO INVÁLIDA')
print(f'A lista dos números foi {lista}.')
print(f'A lista dos números pares foi {parlista}.')
print(f'A lista dos números ímpares foi {imlista}.')

