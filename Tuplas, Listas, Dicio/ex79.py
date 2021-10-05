lista = list()
while True:
    n = int(input('Digite um número:'))
    if n in lista:
        print('\033[0;31mEsse número já está na lista, e não será adicionado!\033[m')
    else:
        lista.append(n)
        print('\033[0;32mNúmero adicionado com sucesso...\033[m')
    r = str(input('Deseja continuar?[S/N]')).strip().upper()
    if r == 'S':
        print('=-' * 35)
    elif r == 'N':
        break
print(f'Você digitou os valores {sorted(lista)}.')






