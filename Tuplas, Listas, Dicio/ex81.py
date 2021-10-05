cont = 0
lista = []
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    cont += 1
    r = str(input('Deseja continuar?[S/N]')).strip()
    if r in 'Ss':
        print('=-'*35)
    elif r in 'Nn':
        break
    else:
        print('Opção inválida')
lista.sort(reverse=True)
print(f'Foram digitados {cont} números')
print(f'A lista em ordem decrescente ficou {lista}.')
if 5 in lista:
    print('O valor 5 apareceu na lista.')
else:
    print('O valor 5 não apareceu na lista.')
