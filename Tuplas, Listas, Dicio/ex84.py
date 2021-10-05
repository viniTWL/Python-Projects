pessoas = []
dados = []
heavy = light = 0
while True:
    pessoas.append(str(input('Digite o nome:')))
    pessoas.append(int(input('Digite seu peso:')))
    if len(dados) == 0:
        heavy = light = pessoas[1]
    else:
        if pessoas[1] > heavy:
            heavy = pessoas[1]
        if pessoas[1] < light:
            light = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Ss':
        print()
    elif r in 'Nn':
        break
print(f'Foram registradas {len(dados)} pessoas.')
print(f'A pessoa mais pesada possui {heavy}kg e se chama ', end='')
for p in dados:
    if p[1] == heavy:
        print(p[0], end='')
print()
print(f'A pessoas mais leve possui {light}kg e se chama ', end='')
for p in dados:
    if p[1] == light:
        print(p[0], end='')







