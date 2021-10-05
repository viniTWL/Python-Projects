dados = dict()
gols = list()
dados['nome'] = str(input('Qual o nome do seu Jogador?')).strip()
dados['partidas'] = int(input('Quantas partidas {} jogou?'.format(dados['nome'])))
for p in range(0, dados['partidas']):
    gols.append(int(input('Quantos gols {} fez na partida {}?'.format(dados['nome'], p+1))))
dados['gols'] = gols
dados['tot'] = sum(gols)
print('-'*40)
print(dados)
print('-'*40)
print('''O jogador se chama {}.
Seus respectivos gols foram {}.
Seu total de gols foi {}.'''.format(dados['nome'], dados['gols'], dados['tot']))
print('-'*40)
print('O jogador {} jogou {} partidas.'.format(dados['nome'], dados['partidas']))
for b, c in enumerate(gols):
    print(f'Na partida {b+1}, fez {c} gol(s).')