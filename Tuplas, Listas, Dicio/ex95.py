dados = dict()
gols = list()
geral = list()
while True:
    dados['nome'] = str(input('Qual o nome do seu Jogador?')).strip()
    dados['partidas'] = int(input('Quantas partidas {} jogou?'.format(dados['nome'])))
    for p in range(0, dados['partidas']):
        gols.append(int(input('Quantos gols {} fez na partida {}?'.format(dados['nome'], p+1))))
    dados['gols'] = gols[:]
    dados['tot'] = sum(gols)
    geral.append(dados.copy())
    dados.clear()
    gols.clear()
    while True:
        r = str(input('Quer continuar cadastrando jogadores?[S/N]')).strip().upper()
        if r in 'SN':
            break
        print('Digite um valor valido')
    if r == 'S':
        print('-'*30)
    if r == 'N':
        break
print('-'*30)
print('cod', end='')
for i in dados.keys():
    print(f'{i:>15}', end='')
print()
print('-'*30)
for k, v in enumerate(geral):
    print(f'{k:>3}', end='')
    for c in v.values():
        print(f'{str(c):<15}', end='')
    print()
print('-'*30)
while True:
    d = int(input('Mostrar dados de qual jogador?(999) interrompe'))
    if d != 999:
        print(f'Levantamento do jogador {geral[d]["nome"]}')
        for n, g in enumerate(geral[d]["gols"]):
            print(f'No jogo {n+1} fez {g} gols')
    if d == 999:
        print('----- PROGRAMA FINALIZADO -----')
        break
    elif d >= len(geral):
        print(f'Não existe jogador registrado com {d}!')



