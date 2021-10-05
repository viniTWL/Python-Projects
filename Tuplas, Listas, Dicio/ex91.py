from random import randint
from operator import itemgetter
from time import sleep
while True:
    r = int(input('\033[0;36mPLAY?\033[m YES (1) NO (0)'))
    if r == 1:
        jogos = dict()
        print('Sorteando os números...')
        sleep(3)
        jogos['player1'] = randint(1, 6)
        jogos['player2'] = randint(1, 6)
        jogos['player3'] = randint(1, 6)
        jogos['player4'] = randint(1, 6)
        for k, v in jogos.items():
            print(f'O {k} jogou {v}')
            sleep(2)
        print('\033[0;36m----- RANKING DA PARTIDA -----\033[m')
        ranking = (sorted(jogos.items(), key=itemgetter(1), reverse=True)) #colocando dicionairio em ordem, key(1) pega keys
        for i, v in enumerate(ranking):
            print(f'O {i+1}º Lugar foi {v[0]} com {v[1]} pontos.')
        print('-'*38)
    elif r == 0:
        print('\033[0;31m----- JOGO FINALIZADO -----')
        break
    else:
        print('Digito inválido')
