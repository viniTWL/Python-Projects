dados = list()
lista = list()
notas = list()
final = list()
cont = 0
while True:
    name = str(input('Nome:'))
    dados.append(name)
    nota1 = float(input('Nota 1:'))
    notas.append(nota1)
    nota2 = float(input('Nota 2:'))
    notas.append(nota2)
    tot = nota1 + nota2 / 2
    dados.append(tot)
    dados.append(notas[:])
    lista.append(dados[:])
    dados.clear()
    notas.clear()
    cont += 1
    r = str(input('Quer continuar?[S/N]')).strip()
    if r in 'Ss':
        print()
    if r in 'Nn':
        break
print('=-'*35)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>9}')
print('-'*25)
for i, c in enumerate(lista):
    print(f'{i:<4}{c[0]:<10}{c[1]:>8.1f}')
while True:
    print('-'*25)
    n = int(input('Deseja mostrar notas de qual aluno? (999 Interrompe)'))
    if n != 999:
        print(f'Notas de {lista[n][0]} foram {lista[n][2]}')
    else:
        break
print('\033[0;31m---- PROGRAMA FINALIZADO ----')
